from setuptools import setup

setup(name='pandas_bin_continous',
      version=' 1.0',
      description='Package to encode continous variables into binned features.',
      url='http://github.com/jtloong/pandas_bin_continous',
      author='Joshua Loong',
      author_email='joshua.t.loong@gmail.com',
      license='MIT',
      packages=['pandas_bin_continous'],
      install_requires=[
          'pandas'
      ],
zip_safe=False)