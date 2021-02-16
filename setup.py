from setuptools import setup, find_packages
from os.path import join, dirname
import socketio

setup(
    name='socketio',
    version=socketio.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=[
        'setuptools>=42',
        'netifaces==0.10.6'
    ],
    author="EvgrDan",
    url="http://zvonobot.ru"
)