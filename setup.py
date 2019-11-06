import setuptools
from version import version_number

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SonaWrap",
    version=version_number,
    author="David Merz",
    author_email="david@merz.dev",
    description="A minimal python wrapper for the Sona systems mobile api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidM42/SonaWrap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)