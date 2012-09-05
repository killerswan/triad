Install the various Android tool packages:
 * Android SDK (r20): http://developer.android.com/sdk/index.html 
 * Android NDK (r7c): http://developer.android.com/tools/sdk/ndk/index.html
   
Run the SDK's `tools/android` utility and choose the particular
version (14) of packages to install.  Leave out proprietary components.

Then set up the environment variables, e.g., in the `~/.bashrc`:

```
export ANDROIDSDK=/code/android/android-sdk-linux
export ANDROIDNDK=/code/android/android-ndk-r7c
export ANDROIDNDKVER=r7c
export ANDROIDAPI=14

PATH="$ANDROIDNDK:$ANDROIDSDK/tools:$ANDROIDSDK/platform-tools:$PATH
```

Then install Eclipse via `apt-get` (eclipse-platform, eclipse-jdt,
and eclipse-cdt), then within Eclipse, manually install the ADT plugin.

(Assuming Kivy was already installed and works on Ubuntu...)

Python for Android can be setup from the git repository:
https://github.com/kivy/python-for-android

Prerequisites are listed here --
http://python-for-android.readthedocs.org/en/latest/prerequisites/ --
including the Ubuntu packages:
`build-essential patch git-core ccache ant ia32-libs and libc6-dev-i386`.
Not listed there, but required, was `python-pip`.
Then `cython` and `jinja2` should be installed.

Finally, in the python-for-android directory, to build the system: 
```
./distribute.sh -m "kivy"
cd dist/default
```

Then to build a package like this one:
```
./build.py --dir /code/triad/kivy/ --package org.kevincantu.triad --name "Triad" --version 0.2 debug
```

To build AND install:
```
./build.py --dir /code/triad/kivy/ --package org.kevincantu.triad --name "Triad" --version 0.2 debug installd
```

Or manually install:
```
adb install -r bin/Triad-0.2-debug.apk
```

Of course, at this point it looks very ugly, but this is a start!


-Kevin, September 2012


