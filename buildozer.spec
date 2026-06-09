[app]
title = Jarvis Controller
package.name = jarviscontroller
package.domain = org.jarvis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Упростили до 3.11, чтобы избежать конфликтов рецептов
requirements = python3==3.11,hostpython3==3.11,kivy==2.3.0,kivymd,requests

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET

# НАСТРОЙКИ ПУТЕЙ (Переносим управление в GitHub Actions workflow)
# buildozer автоматически подхватит ANDROID_NDK_HOME и P4A_dir из env
# android.ndk_path = 
# p4a.source_dir = 

[buildozer]
log_level = 2
warn_on_root = 1
