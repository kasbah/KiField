#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import kifield
import unittest


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'future >= 0.15.0',
    'openpyxl >= 2.3.2',
]

def kifield_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name='kifield',
    version=kifield.__version__,
    description="Module and utilities for manipulating part fields in KiCad files.",
    long_description=readme + '\n\n' + history,
    author=kifield.__author__,
    author_email=kifield.__email__,
    url='https://github.com/xesscorp/kifield',
#    packages=['kifield',],
    packages=setuptools.find_packages(),
    entry_points={'console_scripts':['kifield = kifield.__main__:main']},
    package_dir={'kifield':
                 'kifield'},
    include_package_data=True,
    package_data={'kifield': ['*.gif', '*.png']},
    scripts=[],
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='kifield',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
