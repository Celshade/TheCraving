"""Setup file for distribution"""

from os import path
from setuptools import setup
from setuptools import find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TheCraving',
    version='3.6.3',
    description='A simple text-based adventure game',
    long_description=long_description,
    long_description_content_type='text/plain',
    url='https://github.com/Celshade/The-Craving',
    author='Danny Collins aka Celshade',
    author_email='ggcelshade@gmail.com',
    classifiers=[
        'Developement Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Game Developement :: Game Programming',
        'License :: OSI approved :: MIT License',
        'Programming Language :: Python :: 3.6'
        ],
    keywords='game textadventure thecraving',
    packages=find_packages(),
    project_urls={
        'Bug Reports': 'https://github.com/Celshade/The-Craving/issues',
        'Source': 'https://github.com/Celshade/The-Craving'
    }

)
