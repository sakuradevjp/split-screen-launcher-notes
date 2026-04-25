// Render mockup_split.html → screenshots/{lang}/4_split.png for each
// language in mockup_captions.json. Uses puppeteer from NotiKeep's
// node_modules to avoid an extra install.
const puppeteer = require('C:/Users/ryo_d/notikeep/store_screenshots/node_modules/puppeteer');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const captions = JSON.parse(fs.readFileSync(path.join(ROOT, 'mockup_captions.json'), 'utf8'));
const languages = process.argv.slice(2).length
  ? process.argv.slice(2)
  : Object.keys(captions);

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 2400, deviceScaleFactor: 1 });

  const htmlPath = `file://${path.resolve(ROOT, 'mockup_split.html').replace(/\\/g, '/')}`;
  await page.goto(htmlPath, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 600));

  for (const lang of languages) {
    const c = captions[lang];
    if (!c) {
      console.log(`SKIP ${lang}: no captions`);
      continue;
    }
    await page.evaluate((c) => {
      document.querySelectorAll('[data-i18n]').forEach((el) => {
        const k = el.getAttribute('data-i18n');
        if (c[k] !== undefined) el.textContent = c[k];
      });
    }, c);

    const dir = path.join(ROOT, lang);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    // Output as 3.png to match capture_device.ps1's naming (1=main, 2=create, 3=split-mockup).
    const out = path.join(dir, '3.png');
    const phone = await page.$('#phone');
    await phone.screenshot({ path: out });
    console.log(`wrote ${path.relative(ROOT, out)}`);
  }

  await browser.close();
})();
