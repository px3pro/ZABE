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
        "pandas==2.0.3",
        "numpy==1.24.3"
    ],
    author="ZABE Inc.",
    description="ZABE SDK for privacy-first AI (proprietary core)",
    url="https://github.com/px3pro/ZABE",
    package_data={
        'zabesdk': ['zabe_model.tflite', 'plugins/*.py'],
    },
)