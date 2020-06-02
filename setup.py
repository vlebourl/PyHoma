"""
Install pyhoma
"""

from os.path import exists
from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='pyhoma',
    version=find_version('pyhoma', '__init__.py'),
    url='http://github.com/vlebourl/tahoma-api/',
    license='Apache Software License',
    author='Vincent Le Bourlot',
    install_requires=['requests>=2.0'],
    author_email='vlebourl@gmail.com',
    description='pyhoma - Python connect to Tahoma REST API',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    packages=find_packages(),
    keywords='tahoma somfy io covers senors api',
    platforms='any'
)