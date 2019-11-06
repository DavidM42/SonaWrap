import os
from version import version_number

# from pip._internal import main
# try:
#     import twine
# except ImportError:
#     main(['install', 'twine'])

print("Current version is " + version_number)

input("Update version number in setup.py and press enter")

os.system('python3 setup.py sdist bdist_wheel')
os.system('python3 -m twine upload dist/SonaWrap-' + version_number + '*')