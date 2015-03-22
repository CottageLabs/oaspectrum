from setuptools import setup, find_packages

setup(
    name = 'oaspectrum',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [
        "octopus==1.0.0",
        "esprit",
        "Flask"
    ],
    url = 'http://cottagelabs.com/',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'Open Access Spectrum',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
