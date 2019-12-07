import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ucal_client',
    version='0.1.0',
    python_requires='>3.5.0',
    packages=['ucal_client'],
    description='Client for Ucal Manager Server',
    long_description=README,
    url='https://bitbucket.com/zimka/ucal_manager',
    author='Boris Zimka, Igor Stepanenko',
    author_email='zimka@phystech.edu, igor.stepanenko@phystech.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research'
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only'
        'Topic :: Scientific/Engineering'
    ],
)
