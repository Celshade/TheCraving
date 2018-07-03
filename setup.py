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
    version='0.2.0b1',
    description='A simple text-based adventure game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Celshade/The-Craving',
    author='Danny Collins aka Celshade',
    author_email='ggcelshade@gmail.com',
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Game Development',
        'License :: OSI approved :: MIT License',
        'Programming Language :: Python :: 3.6'
        ],
    python_requires='>=3',
    keywords='game textadventure thecraving',
    packages=find_packages(),
    project_urls={
        'Bug Reports': 'https://github.com/Celshade/The-Craving/issues',
        'Source': 'https://github.com/Celshade/The-Craving'
    }
)
