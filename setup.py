#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'requests>=2'
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(smallsam): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='pymyair',
    version='0.2.1',
    description="A simple Python API that wraps the HTTP based API exposed by the MyPlace service that runs on Advantage Air supplied Android tablets.",
    long_description=readme + '\n\n' + history,
    author="Sam Richards",
    author_email='me@smallsam.com',
    url='https://github.com/davidcfk/pymyair.git',
    packages=find_packages(include=['pymyair']),
    entry_points={
        'console_scripts': [
            'myair=pymyair.cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pymyair',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
