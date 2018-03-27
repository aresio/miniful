from distutils.core import setup
setup(
  name = 'minuful',
  packages = ['miniful'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Minimal Fuzzy Library',
  author = 'Marco S. Nobile',
  author_email = 'nobile@disco.unimib.it',
  url = 'https://github.com/aresio/stfu', # use the URL to the github repo
  #download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['fuzzy logic', 'sugeno', 'reasoner'], # arbitrary keywords
  license='LICENSE.txt',
  long_description=open('README.md').read(),
  install_requires=[
        "numpy >= 1.12.0",
        "scipy >= 1.0.0"
    ],
  #include_package_data=True,
  classifiers = ['Programming Language :: Python :: 2.7'],
 # package_data={'fstpso': ['pso_1st_half_2.fcl', 'pso_2nd_half_2.fcl'], },
)