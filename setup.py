from distutils.core import setup

setup(
    name='imdb-crawler',
    version='1.0.0',
    author='Nicolas Landier',
    author_email='nicolas.landier@gmail.com',
    packages=['crawler', 'crawler.test'],
    scripts=['bin/Crawler.py','bin/GenerateDB.py'],
    url='https://github.com/landier/imdb-crawler',
    license='LICENSE.txt',
    description='IMDB crawler to get data to create a local movie database.',
    long_description=open('README.md').read(),
    install_requires=[
        ],
)