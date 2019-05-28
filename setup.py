from setuptools import setup

setup(name='Slob',
      version='1.0.2',
      description='Read-only compressed data store',
      author='Igor Tkach',
      author_email='itkach@gmail.com',
      url='http://github.com/itkach/slob',
      license='GPL3',
      py_modules=['slob'],
      install_requires=['PyICU >= 1.5'],
      entry_points={'console_scripts': ['slob=slob:main']})
