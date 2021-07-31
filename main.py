import os

os.system("pip install --upgrade pip")
os.system("pip install wheel")
os.system("pip install twine")
os.system("python pyhance/setup.py sdist bdist_wheel")
os.system("twine upload dist/*")