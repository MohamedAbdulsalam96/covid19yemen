# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in covid19yemen/__init__.py
from covid19yemen import __version__ as version

setup(
	name='covid19yemen',
	version=version,
	description='covid19yemen',
	author='Ahmed Mohammed Alkuhlani',
	author_email='aalkuhlani95@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
