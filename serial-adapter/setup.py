from setuptools import setup, find_packages
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bootstrap/bootstrap.py').read(),
    re.M
    ).group(1)

with open('README.rst') as f:
    readme = f.read()

with open('../LICENSE') as f:
    license = f.read()

setup(
    name='serial_adapter',
    version=version,
    description='Serial open zwave adapter package.',
    long_description=readme,
    author='Michal Valovcik',
    author_email='valovcikm@gmail.com',
    url='https://github.com/vychodnar/serial-zwave/serial-adapter',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)