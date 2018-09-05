"""Setup file for distribution"""

from os import path
from codecs import open
from setuptools import setup
from setuptools import find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TheCraving',
    version='2.0.0',
    packages=find_packages(),
    description='A simple text-based adventure game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Celshade/TheCraving',
    author='Danny Collins aka Celshade',
    author_email='ggcelshade@gmail.com',
    license="MIT License",
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
    python_requires='>=3',
    install_requires='pygame>=1.9.3',
    keywords='game textadventure thecraving',
    project_urls={
        'Bug Reports': 'https://github.com/Celshade/TheCraving/issues/9',
        'Comments': 'https://github.com/Celshade/TheCraving/issues/10',
        'Source': 'https://github.com/Celshade/TheCraving'
    }
)
