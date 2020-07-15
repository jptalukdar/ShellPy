from setuptools import setup,find_packages

LIST = find_packages(where='ShellPy')

LIST = ['ShellPy.'+str(item) for item in LIST]
print(LIST)
setup(name='ShellPy',
version='0.1',
description='Testing installation of Package',
url='#',
author='Jyotiplaban Talukdar',
author_email='work.jyotiplaban@gmail.com',
license='MIT',
packages=LIST,
zip_safe=False)