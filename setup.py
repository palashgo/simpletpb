#!/usr/bin/env python
# -*- coding: utf-8 -*
from setuptools import setup


setup(
        name='simpletpb',
        description='Magnet scrapper for The Pirate Bay',
        version='0.1',
        python_requires='>=3',
        url='https://github.com/pabloriutort/simpletpb.git',
        install_requires=['requests','beautifulsoup4'],
        license='MIT',
        author='Pablo Riutort',
        author_email='pablo.riutort@gmail.com',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            ],
)
