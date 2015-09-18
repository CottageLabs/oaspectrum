import sys
from setuptools import setup, find_packages

setup(
    name = 'oaspectrum',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [
        "octopus==1.0.0",
        "esprit",
        # "Flask==0.9"
    ] + (["setproctitle", "newrelic==2.54.0.41", "gunicorn==19.3.0"] if "linux" in sys.platform else []),
    url = 'http://cottagelabs.com/',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'Open Access Spectrum',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
