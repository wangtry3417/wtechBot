from setuptools import setup, find_packages

setup(
    name='wchat',
    version='1.0',
    description='A package for wchat',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'random2'
    ],
)
