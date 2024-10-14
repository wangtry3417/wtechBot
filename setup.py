from setuptools import setup, find_packages

setup(
    name='wchat',
    version='1.2',
    description='A package for wchat,and this is a wchat-api',
    author='WTech',
    author_email='wangtry3417@gmail.com',
    packages=find_packages(),
    install_requires=[
        'python-socketio',
        'asyncio',
        'aiohttp',
        'colorama'
    ],
)
