from setuptools import setup, find_packages

setup(
    name='wchat',
    version='1.0',
    description='A package for wchat',
    author='Wangtry',
    author_email='wangtry3417@gmail.com',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'random2'
    ],
)
