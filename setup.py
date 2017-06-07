from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='jena',
   version='0.1',
   description='Wrapper for serial communication with Jena piezoelectric controllers',
   license="MIT",
   long_description=long_description,
   author='Martin Klein Schaarsberg',
   author_email='martinkleinschaarsberg@gmail.com',
   url="http://readthedocs.org/projects/jena/",
   packages=['jena'],  #same as name
   install_requires=['pyserial', 'numpy>=1.7.0','pytest'], #external packages as dependencies
)