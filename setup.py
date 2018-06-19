from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n' +
    'Contributors\n' +
    '============\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n'
)

setup(name='medialog.mobilethemeThree',
      version=version,
      description="A diazo theme for zettwerk.mobiletheming",
      long_description=long_description,
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='mobiletheming plone zetterk',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      maintainer='Leonardo Caballero',
      maintainer_email='leonardocaballero@gmail.com',
      url='http://github.com/espenmn/medialog.mobilethemeThree',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'ftw.mobilenavigation',
          'plone.api',
          'plone.app.themingplugins',
          'z3c.jbot',
          'zettwerk.mobiletheming',
          
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
