import sys
import logging as log
from config import configuration

requests_logger = log.getLogger('requests.packages.urllib3')
requests_logger.setLevel(log.DEBUG)
requests_logger.propagate = True

root = log.getLogger()
root.setLevel(log.DEBUG)
formatter = log.Formatter('%(asctime)s - %(name) - %(levelname)s - %(message)s')

ch = log.StreamHandler(sys.stdout)
ch.setLevel(log.INFO)
ch.setFormatter(formatter)
root.addHandler(ch)

fh = log.FileHandler(configuration['log']['location'])
fh.setLevel(log.DEBUG)
fh.setFormatter(formatter)
root.addHandler(fh)
