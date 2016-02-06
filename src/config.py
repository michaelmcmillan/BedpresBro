import os
from os.path import dirname, abspath, join
from configparser import ConfigParser, ExtendedInterpolation

configuration = ConfigParser(interpolation=ExtendedInterpolation())
root_directory = dirname(dirname((abspath(__file__))))

if not os.environ.get('TEST'):
    location = join(root_directory, 'config')
else:
    location = join(root_directory, 'test', 'test_config')

configuration.read(location)
