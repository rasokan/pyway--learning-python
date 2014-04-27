## error?
try:
    from setuptools import setup
except:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'authon': 'archie',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'chris.void.92@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'package': ['ex47'],
    'scripts':[],
    'name': 'ex47'
}

setup(**config)