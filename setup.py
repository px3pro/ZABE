from setuptools import setup, find_packages

setup(
    name="zabesdk",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tensorflow==2.18.0",
        "prophet==1.1.5",
        "scikit-learn==1.3.2",
        "torch==2.3.1",
        "pandas==2.2.2",  # Updated to a compatible version
        "numpy==1.26.4"   # Updated to a compatible version
    ],
    author="ZABE Inc.",
    description="ZABE SDK for privacy-first AI",
    url="https://github.com/px3pro/ZABE",
)