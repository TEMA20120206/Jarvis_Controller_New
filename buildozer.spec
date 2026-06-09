[app]
title = Jarvis Controller
package.name = jarviscontroller
package.domain = org.jarvis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Требования к архитектуре проекта
requirements = python3==3.11,hostpython3==3.11,kivy==2.3.0,kivymd,requests

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Жесткие параметры Android SDK/NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.1
android.permissions = INTERNET

# Пути контролируются переменными окружения в Workflow
# android.ndk_path = 
# p4a.source_dir = 

[buildozer]
log_level = 2
warn_on_root = 1
