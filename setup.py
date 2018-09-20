import setuptools

with open("README.md", "r") as f:
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
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Other Audience",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
)