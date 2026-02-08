[app]
title = KivyApp
package.name = kivyapp
package.domain = org.example

# ★これが無いと以前の「version / version.regex が必要」エラーになる
version = 0.1

# リポジトリ直下に main.py がある前提
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,gif,atlas,ttf,otf,txt,json,wav,mp3,ogg

# 入口ファイル
source.main = main.py

# Kivyアプリの基本（必要に応じて追加）
requirements = python3,kivy

# 画面向き（必要なら landscape に）
orientation = portrait

# Android設定（安定寄り）
android.api = 33
android.minapi = 21
android.ndk = 25b

# ★GitHub Actionsで止まりがちなSDKライセンスを自動同意
android.accept_sdk_license = True

# 出力形式
android.archs = arm64-v8a, armeabi-v7a

# 権限（必要なものだけ残す）
android.permissions = INTERNET

# buildozer のログ量
log_level = 2
