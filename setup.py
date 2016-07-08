from setuptools import setup

setup(name='epitran',
      version='0.2',
      description='Tools for transcribing languages into IPA.',
      url='http://github.com/dmort27/epitran',
      download_url='http://github.com/dmort27/epitran/tarball/0.2',
      author='David R. Mortensen',
      author_email='dmortens@cs.cmu.edu',
      license='MIT',
      install_requires=['setuptools',
                        'unicodecsv',
                        'regex',
                        'subprocess32',
                        'panphon>=0.3'],
      scripts=['epitran/bin/epitranscribe.py',
               'epitran/bin/uigtransliterate.py',
               'epitran/bin/detectcaps.py',
               'epitran/bin/connl2ipaspace.py',
               'epitran/bin/connl2engipaspace.py',
               'epitran/bin/testvectorgen.py',
               'epitran/bin/transltf.py'],
      packages=['epitran'],
      package_dir={'epitran': 'epitran'},
      package_data={'epitran': ['data/*.csv', 'data/*.json',
                                'data/pre/*.csv', 'data/post/*.csv',
                                'data/space/*.csv']},
      zip_safe=True
      )
