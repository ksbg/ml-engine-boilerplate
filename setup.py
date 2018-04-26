"""This setup file is needed to package the application for gcloud deployment."""
from setuptools import setup, find_packages

setup(
    name='trainer',
    version='0.1',
    author='ksbg',
    author_email='kevin@ksbg.io',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    description='ML engine boilerplate')
