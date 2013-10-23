from setuptools import setup
import sys

from pyleus import __version__


extra_install_requires = []
if sys.version_info < (2, 7):
    extra_install_requires.append('argparse==1.2.1')


setup(
    name='pyleus',
    version=__version__,
    author='Patrick Lucas',
    author_email='plucas@yelp.com',
    description='Standard library and deployment tools for using Python with Storm',
    packages=['pyleus'],
    scripts=['scripts/pyleus'],
    install_requires=extra_install_requires,
)
