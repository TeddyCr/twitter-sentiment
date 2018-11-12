import setuptools
from setuptools.command.install import install

import os
import sys

VERSION = '0.0.591'

with open("README.md", "r") as f:
    long_description = f.read()

class VerifyVersion(install):
    """
    Custom command to verify the package version matches the git tag version
    """
    description = "Command ran to check if the new uploaded version matches the git tag"
    
    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = f'Tag {tag} does not match current version {VERSION} in setup.py'
            sys.exit(info)

setuptools.setup(
    name="twitter-sentiment",
    version=VERSION,
    author="Teddy Crepineau",
    author_email="teddy.crepineau@gmail.com",
    description="Twitter sentiment is a Python library leveraging NLP "
                "and the Twitter API to determine the emotion of a tweet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeddyCr/twitter-sentiment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Other Audience",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    cmdclass= {
        'verify': VerifyVersion,
    }
)
