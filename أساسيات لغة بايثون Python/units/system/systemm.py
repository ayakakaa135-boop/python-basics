import sys
print(sys.platform)
print(sys.version)
print(sys.getwindowsversion())
if sys.platform.startswith('linux'):
    print('you are using linux')
elif sys.platform.startswith('darwin'):
    print('you are using macos')
elif sys.platform.startswith('win32'):
    print('you are using windows')
