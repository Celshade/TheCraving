"""Setup file for distribution"""

from os import path
# from cx_Freeze import setup, Executable
from setuptools import setup
from setuptools import find_packages

# build_exe_options = {"packages": ["thecraving"]}
here = path.abspath(path.dirname(__file__))

# Meta Data
NAME = 'TheCraving'
DESCRIPTION = 'A simple, text-based, adventure game'
URL = 'https://github.com/Celshade/TheCraving'
EMAIL = 'ggcelshade@gmail.com'
AUTHOR = 'Danny Collins aka Celshade'
REQUIRES_PYTHON = '>=3.6'
VERSION = '2.0.1'
REQUIRES = ['pygame']

# README handling
try:
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f'\n{f.read()}'
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRES,
    include_package_data=True,
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    # options={"build_exe": build_exe_options},
    # executables=[Executable("thecraving//thecraving.py")],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Terminal/Shell',
        'Intended Audience :: End Users/Desktop'
        'Intended Audience :: Developers',
        'Topic :: Game Development',
        'License :: OSI approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.6'
        ],
    keywords='game textadventure thecraving',
    project_urls={
        'Bug Reports': 'https://github.com/Celshade/TheCraving/issues/9',
        'Comments': 'https://github.com/Celshade/TheCraving/issues/10',
        'Source': 'https://github.com/Celshade/TheCraving'
    }
)
