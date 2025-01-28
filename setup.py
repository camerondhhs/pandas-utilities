from setuptools import setup, find_packages

setup(
    name="pandas_utilities", 
    version="0.1.0",
    description="A collection of utilities for pandas data processing",
    author="Cameron",
    url="https://github.com/camerondhhs/pandas-utilities",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0",
        "nltk>=3.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

