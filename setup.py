#! /usr/bin/env python
#
# Copyright (C) 2015 Chris Holdgraf
# <choldgraf@gmail.com>
#
# Adapted from MNE-Python

import os
import setuptools
from numpy.distutils.core import setup
from mnespikes import __version__

descr = """A quick module to help mne-spikesing files using python."""

DISTNAME = 'mne-spikes'
DESCRIPTION = descr
MAINTAINER = 'Chris Holdgraf'
MAINTAINER_EMAIL = 'choldgraf@gmail.com'
URL = 'https://github.com/choldgraf/mne-spikes'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/choldgraf/mne-spikes'
VERSION = __version__


if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          include_package_data=False,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=open('README.rst').read(),
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=['Intended Audience :: Science/Research',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved',
                       'Programming Language :: Python',
                       'Topic :: Software Development',
                       'Topic :: Scientific/Engineering',
                       'Operating System :: OSX'],
          platforms='any',
          packages=['mnespikes'],
          package_data={},
          scripts=[])
