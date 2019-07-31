from distutils.core import setup
setup(
  name = 'miniful',
  packages = ['miniful'], # this must be the same as the name above
  version = '0.0.5',
  description = 'Minimal Fuzzy Library',
  author = 'Marco S. Nobile',
  author_email = 'nobile@disco.unimib.it',
  url = 'https://github.com/aresio/stfu', # use the URL to the github repo
  keywords = ['fuzzy logic', 'sugeno', 'reasoner'], # arbitrary keywords
  license='LICENSE.txt',
  install_requires=[
        "numpy >= 1.12.0",
        "scipy >= 1.0.0"
    ],
  classifiers = ['Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3.6'],
)