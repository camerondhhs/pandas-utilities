from setuptools import setup, find_packages

setup(
    name="pandas-utilities",  # Replace with your desired package name
    version="0.1.0",  # Increment this for each release
    description="A collection of utilities for pandas data processing",
    author="Cameron",
    author_email="your_email@example.com",  # Replace with the maintainer's email
    url="https://github.com/camerondhhs/pandas-utilities",  # GitHub repo URL
    packages=find_packages(),  # Automatically find all packages and subpackages
    install_requires=[
        "pandas>=1.0",  # Add your project's dependencies
        "nltk>=3.0",    # If `nltk` is required
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust license if needed
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Adjust Python version compatibility
)

