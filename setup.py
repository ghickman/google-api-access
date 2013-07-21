# -*- coding: utf-8 -*-
"""
google-api-access
~~~~~~~~~~~~~~~~~

A simple utility script to help you generate a refresh token so your application
can use Google API(s) without user interaction.
For more information see http://ghickman.co.uk/2013/07/21/google-api-offline-access.html


Installation
-----------

    pip install google-api-access


Usage
-----

    google-api-access
"""
from setuptools import setup


setup(
    name='google-api-auth',
    version='0.1',
    description='Generate a refresh token for Google API access in applications where a user isn\'t present',
    long_description=__doc__,
    author='George Hickman',
    author_email='george@ghickman.co.uk',
    url='http://github.com/ghickman/google-api-access',
    license='MIT',
    py_modules=['google_api_access'],
    entry_points={'console_scripts': ['google-api-auth=google_api_auth:run']},
    classifiers=(
        'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
    ),
    install_requires=('requests>=1.2.3'),
)
