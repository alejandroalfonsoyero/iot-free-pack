#!/usr/bin/python3
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    description = long_description.split('\n', 1)[0]

setup(
    name="iot_free_pack",
    version="1.0.0",
    description=description,
    long_description=long_description,
    author="Alejandro Alfonso",
    author_email="alejandroalfonso1994@gmail.com",
    url="",
    packages=find_packages(exclude=['tests']),
    entry_points={},
    install_requires=[]
)