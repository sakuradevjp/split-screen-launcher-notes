# Capture main + create-pair screens from a connected debug-build SSL on
# every locale we ship. Assumes:
#   - debug APK installed
#   - seed pairs already pushed
#   - state already set to trial_active
#
# Output: screenshots/{slug}/1.png (main), 2.png (create pair form)
# Note: 3.png is the mockup split view, generated separately.
#
# Tap coordinates calibrated for Pixel 9a (1080x2400):
#   FAB+ = (965, 2055)
#   "Create pair" menu item (top of pop-up) = (760, 1790)

param(
  [string[]]$Slugs
)

$ErrorActionPreference = "Stop"

$ROOT = "C:\Users\ryo_d\split-screen-launcher-notes-repo\screenshots"
$PKG = "com.ryodev.splitscreen"

# (slug, bcp47) for cmd locale set-app-locales
$ALL_LOCALES = @(
  @("en",    "en-US"),
  @("ja",    "ja-JP"),
  @("ko",    "ko-KR"),
  @("zh-CN", "zh-CN"),
  @("zh-TW", "zh-TW"),
  @("es",    "es-ES"),
  @("pt-BR", "pt-BR"),
  @("fr",    "fr-FR"),
  @("de",    "de-DE"),
  @("it",    "it-IT"),
  @("ru",    "ru-RU"),
  @("ar",    "ar"),
  @("hi",    "hi-IN"),
  @("th",    "th"),
  @("vi",    "vi")
)

$targets = if ($Slugs) {
  $ALL_LOCALES | Where-Object { $Slugs -contains $_[0] }
} else {
  $ALL_LOCALES
}

# Keep screen on while USB-connected so the captures don't go black.
adb shell svc power stayon usb | Out-Null
adb shell input keyevent KEYCODE_WAKEUP | Out-Null
adb shell wm dismiss-keyguard | Out-Null

# Make sure state is fresh (trial_active = no Pro-ended dialog, pairs visible)
adb shell am broadcast -a com.ryodev.splitscreen.DEBUG_SET_STATE -e state trial_active -n com.ryodev.splitscreen/.DebugReceiver | Out-Null

foreach ($pair in $targets) {
  $slug = $pair[0]
  $bcp = $pair[1]
  $dir = Join-Path $ROOT $slug
  New-Item -ItemType Directory -Force -Path $dir | Out-Null

  Write-Host "[$slug] setting locale $bcp..." -ForegroundColor Cyan
  # Re-wake every iteration; idle waits can put screen back to sleep.
  adb shell input keyevent KEYCODE_WAKEUP | Out-Null
  adb shell cmd locale set-app-locales $PKG --locales $bcp | Out-Null
  adb shell am force-stop $PKG | Out-Null
  Start-Sleep -Milliseconds 400

  # Re-apply state (force-stop wipes any in-memory state). Trial_active
  # is the cleanest baseline to avoid blocking dialogs.
  adb shell am broadcast -a com.ryodev.splitscreen.DEBUG_SET_STATE -e state trial_active -n com.ryodev.splitscreen/.DebugReceiver | Out-Null
  Start-Sleep -Milliseconds 200

  # Launch
  adb shell monkey -p $PKG -c android.intent.category.LAUNCHER 1 *> $null
  Start-Sleep -Seconds 3

  # Main screen
  adb shell screencap -p /sdcard/_main.png | Out-Null
  adb pull /sdcard/_main.png "$dir\1.png" 2>&1 | Out-Null
  Write-Host "  -> 1.png (main)"

  # Tap FAB+ to open "create pair / create folder" pop-up
  adb shell input tap 965 2055 | Out-Null
  Start-Sleep -Milliseconds 800

  # Tap top menu item ("Create pair")
  adb shell input tap 760 1790 | Out-Null
  Start-Sleep -Seconds 2

  # Create-pair screen
  adb shell screencap -p /sdcard/_create.png | Out-Null
  adb pull /sdcard/_create.png "$dir\2.png" 2>&1 | Out-Null
  Write-Host "  -> 2.png (create form)"

  # Back to main for next iteration
  adb shell input keyevent KEYCODE_BACK | Out-Null
  Start-Sleep -Milliseconds 400
}

# Cleanup tmp files on device
adb shell rm /sdcard/_main.png /sdcard/_create.png 2>&1 | Out-Null
Write-Host "Done." -ForegroundColor Green
