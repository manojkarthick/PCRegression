# _*_ coding: utf-8 _*_
from distutils.core import setup
from setuptools import setup

SCIPY_MIN_VERSION = '0.13.3'
NUMPY_MIN_VERSION = '1.8.2'

setup(
    name='PCRegression',
    version='0.1.1',
    author='Karanjit Singh Tiwana, Arin Ghosh, Manoj Karthick',
    author_email='manojkarthick@ymail.com',
    url='https://github.com/manojkarthick/PCRegression',
    license='MIT License',
    description='Python package for building a principal components regression model using scikit-learn',
    py_modules=['PCRegression'],
    keywords = ['machine learning', 'sklearn', 'pcr','pca','regression', 'dimensionality reduction'], # arbitrary keywords
    classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'numpy>={0}'.format(NUMPY_MIN_VERSION),
        'scipy>={0}'.format(SCIPY_MIN_VERSION),
        'scikit-learn'
    ],
)