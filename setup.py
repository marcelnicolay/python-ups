# coding: utf-8 -*-
from setuptools import setup


setup(
    name='python-ups',
    version='0.0.1',
    description="UPS shipping interface",
    keywords=['ups', 'shipping'],
    author='Marcel Nicolay',
    author_email='marcel.nicolay@gmail.com',
    url='http://github.com/marcelnicolay/python-ups',
    license='OSI',
    install_requires=open("requirements.txt").read().split("\n"),
    packages=['ups'],
    test_suite="nose.collector"
)
