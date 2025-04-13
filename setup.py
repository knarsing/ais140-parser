#This file describes how to build and install the package.

from setuptools import setup, find_packages

setup(
    name='ais140-parser',
    version='1.0.0',
    description='AIS140 Protocol Parser',
    author='Narsing Pimpale',
    author_email='narsing.pimple@gmail.com',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
