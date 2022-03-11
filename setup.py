#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aab",
    version="1.0.0-dev.1",
    description="Anki Add-on Builder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glutanimate/anki-addon-builder",
    author="Aristotelis P. (Glutanimate)",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
    ],
    keywords="anki development build-tools",
    packages=["aab"],
    python_requires=">=3.6",
    install_requires=["jsonschema", "whichcraft"],
    # e.g. $ pip install aab[qt6]
    extras_require={
        "qt6": ["PyQt6>=6.2.2"],
        "qt5": ["PyQt5>=5.12"],
    },
    entry_points={
        "console_scripts": [
            "aab=aab.cli:main",
        ],
    },
    package_data={"aab": ["schema.json"]},
    project_urls={
        "Bug Reports": "https://github.com/glutanimate/anki-addon-builder/issues",
        "Funding": "https://glutanimate.com/support-my-work/",
        "Source": "https://github.com/glutanimate/anki-addon-builder",
    },
)
