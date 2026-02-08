[app]
# アプリ名（表示名）
title = SimpleCounter

# パッケージ名（英小文字推奨・スペース不可）
package.name = simplecounter

# ドメイン（逆ドメイン形式）
package.domain = org.sir.simplecounter

# ソースの場所（リポジトリ直下なら .）
source.dir = .

# 取り込む拡張子
source.include_exts = py,kv,png,jpg,jpeg,ttf,otf

# ★最重要：起動ファイル
entrypoint = main.py

# ★最重要：バージョン（ないとエラーになる）
version = 0.1

# 必要ライブラリ（まずは最小）
requirements = python3,kivy

# 画面向き
orientation = portrait

# 全画面（不要なら 0）
fullscreen = 1

# 権限（ネット不要なら消してOK）
android.permissions = INTERNET

# Android API（まずはこのままでOK）
android.api = 33
android.minapi = 21

# アーキテクチャ（まずは armeabi-v7a と arm64-v8a）
android.archs = armeabi-v7a,arm64-v8a

# ログやデバッグ（困ったら true にしてログ増やす）
log_level = 2

[buildozer]
# （空でOK）
