"""
Setup configuration for LegalInkPack
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="legalinkpack",
    version="0.1.0",
    author="LegalInkPack Team",
    description="Reverse deployable countersurveillance toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joeathan/LegalInkPack",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Dependencies will be added here
    ],
)
