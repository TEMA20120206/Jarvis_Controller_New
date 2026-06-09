[app]
title = Jarvis Controller
package.name = jarviscontroller
package.domain = org.jarvis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Фиксация ветки Python 3.11 без микроверсий для стабильности рецептов
requirements = python3==3.11,hostpython3==3.11,kivy==2.3.0,kivymd,requests

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Базовые настройки Android SDK/NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET

# Пути закомментированы, так как мы управляем ими через GitHub Actions (переменные P4A_dir и ANDROID_NDK_HOME)
# android.ndk_path = 
# p4a.source_dir = 

[buildozer]
log_level = 2
warn_on_root = 1
