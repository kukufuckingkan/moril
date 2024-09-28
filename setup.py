
from setuptools import setup

setup(
    name="moril",
    version="1.0.8",
    description='manden packages',
    author='Ana Keita',
    author_email='keita.kukukhan@gmail.com',    
    packages=['kukukan','conda','memory','query','ali','ana'],
    install_requires=[
        'pandas',
        'sqlalchemy',
        'Pillow'
    ],
    python_requires='>=3.6'
)
