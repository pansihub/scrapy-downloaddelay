from setuptools import setup, find_packages

setup(
    version='0.0.1',
    name='scrapy-downloaddelay',
    description='scrapy downloaddelay plugin',
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
        'scrapy.plugin': [
            'scrapy-downloaddelay = scrapy_downloaddelay.plugin:Plugin',
        ],
    },
)
