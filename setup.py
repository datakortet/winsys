# -*- coding: utf-8 -*-

"""Python tools for the Windows sysadmin
"""

#
# Create a .whl:  python setup.py bdist_wheel (requires pip install wheel)
# development:    python setup.py develop
# pip install:    pip install c:\work\winsys
# pip dev inst:   pip install -e c:\work\winsys
#

classifiers = [line for line in """\
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: System Administrators
License :: OSI Approved :: MIT License
Operating System :: Microsoft :: Windows :: Windows NT/2000
Programming Language :: Python :: 3
Topic :: Utilities
""".split('\n') if line]

import os, sys
import setuptools
from distutils.core import setup, Extension

# import winsys
version = open("VERSION.txt").read().strip()

packages = ['winsys']  #, 'winsys.tests', 'winsys._security', 'winsys.extras']
# ext_modules = [
#     Extension("winsys._change_journal", ["src/_change_journal.c"]),
# ]

  
setup(
    name='WinSys',
    version=version,
    url='http://github.com/tjg/winsys',
    license='LICENSE.txt',
    author='Tim Golden',
    author_email='mail@timgolden.me.uk',
    description=__doc__.strip(),
    long_description=open("README.rst").read(),
    classifiers=classifiers,
    platforms='win32',
    packages=packages,
    ext_modules=[] ## ext_modules
)
