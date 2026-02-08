[app]
title = SimpleCounter
package.name = simplecounter
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0


[buildozer]
log_level = 2
warn_on_root = 0
buildozer.no_chown = True


[android]
# まずは安定重視。端末側で動かすなら debug でOK。
# release にするのは動作確認できてから。
android.api = 33
android.minapi = 21

# ここは触らない（トラブルを増やすだけになりやすい）
# android.ndk = 25b
