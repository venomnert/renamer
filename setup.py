# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='renamer',
    version='1.0',
    description='Extend os rename functionality to include slug.',
    long_description=long_description,
    license='MIT',
    url='https://github.com/venomnert/renamer',
    author='venomnert',
    author_email='venomnert1994@hotmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Windows 10'
    ],
    keywords='setuptools development',  # Optional
    install_requires=['slugify']
)