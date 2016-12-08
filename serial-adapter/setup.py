from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('../LICENSE') as f:
    license = f.read()

setup(
    name='serial_adapter',
    version='0.0.1',
    description='Serial open zwave adapter package.',
    long_description=readme,
    author='Michal Valovcik',
    author_email='valovcikm@gmail.com',
    url='https://github.com/vychodnar/serial-zwave/serial-adapter',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)