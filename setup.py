#!/usr/bin/env python

import os
import sys

from distutils.text_file import TextFile
from skbuild import setup

# Add current folder to path
# This is required to import versioneer in an isolated pip build
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import versioneer  # noqa: E402


with open('README.rst', 'r') as fp:
    readme = fp.read()

with open('HISTORY.rst', 'r') as fp:
    history = fp.read().replace('.. :changelog:', '')


def parse_requirements(filename):
    with open(filename, 'r') as file:
        return TextFile(filename, file).readlines()


requirements = []
dev_requirements = parse_requirements('requirements-dev.txt')

# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])

setup_requires = pytest_runner

setup(
    name='cmake',

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    author='Jean-Christophe Fillion-Robin',
    author_email='jchris.fillionr@kitware.com',

    packages=['cmake'],

    cmake_install_dir='cmake/data',

    entry_points={
        'console_scripts': [
            'cmake=cmake:cmake', 'cpack=cmake:cpack', 'ctest=cmake:ctest'
        ]
    },

    url='https://cmake.org/',
    download_url='https://cmake.org/download',
    project_urls={
        "Documentation": "https://cmake-python-distributions.readthedocs.io/",
        "Source Code": "https://github.com/scikit-build/cmake-python-distributions",
        "Mailing list": "https://groups.google.com/forum/#!forum/scikit-build",
        "Bug Tracker": "https://github.com/scikit-build/cmake-python-distributions/issues",
    },


    description='CMake is an open-source, cross-platform family of '
                'tools designed to build, test and package software',

    long_description=readme + '\n\n' + history,

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Programming Language :: Fortran',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools'
        ],

    license='Apache 2.0',

    keywords='CMake build c++ fortran cross-platform cross-compilation',

    install_requires=requirements,
    tests_require=dev_requirements,
    setup_requires=setup_requires
    )
