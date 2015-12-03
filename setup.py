from setuptools import setup, find_packages
import sys, os


setup(name='abbreviation-resolver',
      version='0.1',
      description="Abbreviation resolver",
      author='Alexander Tkachenko',
      author_email='aleksandr.tkatsenko@ut.ee',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      install_requires=[
        'estnltk==1.3',
        'numpy>=1.10.1',
        'pandas==0.16.2',
        'cached_property==1.2.0',
        'scipy',
        'gensim',
      ],
      entry_points={"console_scripts": ["test_text=abresolver.scripts.test_text:main"]},
)
