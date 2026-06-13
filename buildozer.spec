[app]
title = Jarvis Controller
package.name = jarviscontroller
package.domain = org.jarvis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.0,kivymd==1.2.0,Cython==0.29.33,requests

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
