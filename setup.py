"""
Mulre
=====

Anonymous message board.

"""
from setuptools import setup


setup(
    name='Mulre',
    version='0.0.0',
    url='https://github.com/mulre/mulre',
    author='Jihyeok Seo',
    author_email='limeburst@mul.re',
    description='Anonymous message board',
    long_description=__doc__,
    zip_safe=False,
    packages=['mulre', 'mulre.web'],
    package_data={
        'mulre.web': ['templates/*.*', 'static/*.*']
    },
    install_requires=[
        'Flask == 0.10.1',
        'SQLAlchemy == 0.9.9',
        'boto == 2.36.0',
        'click == 3.3',
    ],
    entry_points={
        'console_scripts': ['mre = mulre.cli:cli'],
    },
)
