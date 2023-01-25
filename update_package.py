import os
from version import version_number

# from pip._internal import main
# try:
#     import twine
# except ImportError:
#     main(['install', 'twine'])

input("Make sure you commented in the dev dependancies in requirements.txt and installed them. Press enter")
print("Current version is " + version_number)

input("Did you update the version number in version.py. If so press enter")

os.system('python3 setup.py sdist bdist_wheel')
os.system('python3 -m twine upload dist/SonaWrap-' + version_number + '*')