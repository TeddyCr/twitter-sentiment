import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="twitter-sentiment",
    version="0.0.1",
    author="Teddy Crepineau",
    author_email="teddy.crepineau@gmail.com",
    description="Twitter sentiment is a Python library leveraging NLP and the Twitter API to determine the emotion of a tweet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeddyCr/twitter-sentiment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)