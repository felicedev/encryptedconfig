from setuptools import setup, find_packages

setup(
    name="encryptedconfig",
    version="0.1.0",
    description="Encrypted configuration manager supporting multiple formats.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="FeliceDev",
    author_email="email@felicedev.com",
    url="https://github.com/felicedev/encryptedconfig",
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "PyYAML",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
