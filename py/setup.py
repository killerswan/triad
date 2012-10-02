from distutils.core import setup

setup(
    name='Triad',
    version='0.2dev',
    packages=['triad',],
    license='ISC License',
    long_description=open('README.md').read(),
)

# TODO: hook nose up to `test` using something better than distutils

