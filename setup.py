from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='alneberg',
      version=version,
      description="Pythonkurs code",
      long_description="""\
Just a silly one""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python Scilifelab',
      author='Johannes Alneberg',
      author_email='johannes.alneberg@scilifelab.se',
      url='example.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=["scripts/getting_data.py"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
