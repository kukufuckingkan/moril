
import setuptools
from setuptools import setup

setup(
    name="moril",
    version="1.0.7",
    description='manden packages',
    author='Ana Keita',
    author_email='keita.kukukhan@gmail.com',    
    packages=['kukukan','conda','memory','query','ali'],
    install_requires=[
        'pandas',
        'sqlalchemy',
        'Pillow'
    ],
    python_requires='>=3.6'
)
