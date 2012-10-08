# coding: utf-8 -*-
from setuptools import setup


setup(
    name='python-ups',
    version='0.0.4',
    description="UPS shipping interface",
    keywords=['ups', 'shipping'],
    author='Marcel Nicolay',
    author_email='marcel.nicolay@gmail.com',
    url='http://github.com/marcelnicolay/python-ups',
    license='OSI',
    packages=['ups'],
    package_data={'ups': ['wsdl/*']},
    install_requires=['suds>=0.4'],
    test_suite="nose.collector"
)
