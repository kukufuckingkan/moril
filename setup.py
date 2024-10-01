
from setuptools import setup

setup(
    name="moril",
    version="2.1.5",
    description='manden packages',
    author='Ana Keita',
    author_email='keita.kukukhan@gmail.com',    
    packages=['kukukan','conda','memory','aminatu','ali','ana'],
    install_requires=[
        'pandas',
        'sqlalchemy',
        'Pillow',
        'openpyxl'
    ],
    python_requires='>=3.9.6'
)
