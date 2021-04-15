from setuptools import setup, find_packages
import sys, os

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
setup(
  name = 'coconutpy',
  version='3.0.0',
  #py_modules = ['coconut.job', 'coconut.metadata'],
  packages=find_packages(exclude=['tests*']),
  author='Coconut',
  author_email='team@coconut.co',
  description='A python wrapper around the Coconut API',
  license='MIT License',
  url='https://coconut.co',
  keywords='coconut video encoding api',
  install_requires=[ "httplib2" ],
	long_description="""Client Library for encoding Videos with Coconut

Coconut is a Video Encoding Web Service built for developers.

For more information:

* Coconut: https://coconut.co
* API Documentation: https://docs.coconut.co
* Twitter: @openCoconut

Changelogs

3.0.0
New pytonh library compatible with Coconut APIv2

2.4.3
Fix Authorization Header:
"TypeError: a bytes-like object is required, not 'str'" was returned before

2.4.2
Don't wait for a 401 challenge to pass the auth token to Coconut APIs.

2.4.0
Implements new Job methods to get info about a job and get metadata (new metadata API).

2.2.0
Added a new method #config to generate a full configuration based on the given parameters. It's especially useful to handle dynamic settings like source or variables that can be set directly in code.

2.0.0
New version of the client library which uses the HeyWatch API v2. This library is not compatible with 1.x

1.0.0
First version

"""
)