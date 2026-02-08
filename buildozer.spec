[app]
title = SimpleCounter
package.name = simplecounter
package.domain = org.sir.simplecounter
version = 0.1

source.dir = .
source.main = main.py

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET

# ★重要：Android SDK 関連
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# ★ライセンス自動同意
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
