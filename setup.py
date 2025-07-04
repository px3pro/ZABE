from setuptools import setup, find_packages
import os

# Dynamically find plugins in src/examples/
plugin_files = []
examples_dir = os.path.join(os.path.dirname(__file__), 'src', 'examples')
for root, dirs, files in os.walk(examples_dir):
    for file in files:
        if file.endswith('.py'):
            plugin_files.append(os.path.relpath(os.path.join(root, file), os.path.dirname(__file__)))

setup(
    name="zabesdk",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': plugin_files},
    install_requires=[
        "tensorflow>=2.18.0",
        "prophet>=1.1.5",
        "scikit-learn>=1.3.2",
        "torch>=2.3.1",
        "pandas>=2.0.3",
        "numpy>=1.24.3"
    ],
    author="ZABE Inc.",
    description="ZABE SDK for privacy-first AI with dynamic plugin support",
    url="https://github.com/px3pro/ZABE",
)