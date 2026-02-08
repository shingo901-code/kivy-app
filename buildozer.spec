[app]
# =========================
# Basic app info
# =========================
title = SimpleCounter
package.name = simplecounter
package.domain = org.sir.simplecounter

# ★必須：これが無いと今回のエラーになります
version = 0.1

# =========================
# Source / entry point
# =========================
source.dir = .
# いちばん安全：ファイル名は main.py にする
source.main = main.py
# もし main.py にリネームできない場合（非推奨）：
# source.main = SimpleCounter.py
# ※ "Simple Counter.py" のようにスペースがある名前は避けてください

source.include_exts = py,kv,png,jpg,jpeg,gif,ttf,otf,wav,mp3,ogg,json,txt

# =========================
# Dependencies
# =========================
# Kivyだけなら通常これでOK
requirements = python3,kivy

# （よく使う追加例：必要ならコメント外す）
# requirements = python3,kivy,requests

# =========================
# App behavior
# =========================
orientation = portrait
fullscreen = 1

# =========================
# Android settings
# =========================
# ネット不要なら INTERNET は消す（権限は少ない方が良い）
# android.permissions = INTERNET
android.permissions =

# AndroidX（最近の環境では付けておくと無難）
android.enable_androidx = True

# ターゲットSDKはビルド環境次第で変動するので、まずは未指定推奨
# android.api = 33
# android.minapi = 21

# もし日本語フォントなど同梱したい場合は assets に入れる
# android.add_src = assets

# アイコン/スプラッシュ（用意できたら）
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# =========================
# Buildozer settings
# =========================
[buildozer]
log_level = 2

# （GitHub Actions等でやり直しを安定させたい時の定番）
warn_on_root = 0
