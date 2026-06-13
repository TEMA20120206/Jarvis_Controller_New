      - name: Setup Android SDK
        run: |
          # Создаём структуру папок
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/cmdline-tools
          
          # Скачиваем свежие command-line tools
          wget -q https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O cmdtools.zip
          unzip -q cmdtools.zip -d $HOME/.buildozer/android/platform/android-sdk/cmdline-tools
          mv $HOME/.buildozer/android/platform/android-sdk/cmdline-tools/cmdline-tools \
             $HOME/.buildozer/android/platform/android-sdk/cmdline-tools/latest
          
          # Создаём симлинк по старому пути, который ищет buildozer
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/tools/bin
          ln -s $HOME/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager \
                $HOME/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager

          # Принимаем лицензии
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/licenses
          printf "24333f8a63b6825ea9c5514f83c2829b004d1fee\nd56f5187479451eabf01fb78af6dfcb131a6481e\n84831b9409646a918e30573bab4c9c91346d8abd" \
            > $HOME/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          printf "84831b9409646a918e30573bab4c9c91346d8abd" \
            > $HOME/.buildozer/android/platform/android-sdk/licenses/android-sdk-preview-license

          # Устанавливаем build-tools и platform
          yes | $HOME/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager \
            --sdk_root=$HOME/.buildozer/android/platform/android-sdk \
            "build-tools;33.0.1" "platforms;android-33" "platform-tools"

      - name: Build APK
        run: buildozer android debug
        env:
          JAVA_HOME: ${{ env.JAVA_HOME_17_X64 }}
          ANDROID_SDK_ROOT: /home/runner/.buildozer/android/platform/android-sdk
