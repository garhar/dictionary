import os
import sys
import ConfigParser
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter

default_settings = {}

config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'settings.cfg')
priv_config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                '.settings.cfg')
config = ConfigParser.RawConfigParser(default_settings)


if os.path.isfile(priv_config_file):
    config.read(priv_config_file)
else:
    config.read(config_file)

def read_config(name, section='dictionary'):
    try:
        return config.get(section, name)
    except:
        return ''


def logger():
    return dictionary_logger


def is_production():
    return read_config('PRODUCTION') == 'True'


def is_debug():
    return read_config('DEBUG') == 'True'


DEFAULT_LOCALE = read_config('DEFAULT_LOCALE')
TMP_DIR = read_config('TMP_DIR')

#  logging configuration
dictionary_logger = logging.getLogger('dictionary')
logger_format = ("%(asctime)s %(levelname)s: %(message)s"
                 " [%(pathname)s:%(lineno)d]")

logger_filename = "%s/dictionary.log" % config.get('dictionary', 'ROOT_DIR')
vlh = RotatingFileHandler(logger_filename, mode='a', maxBytes=50485760,
                          backupCount=5)
vlh.setFormatter(Formatter(logger_format))

if is_debug():
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(Formatter(logger_format))
    dictionary_logger.addHandler(ch)
    vlh.setLevel(logging.DEBUG)
    dictionary_logger.setLevel(logging.DEBUG)
else:
    vlh.setLevel(logging.INFO)
    dictionary_logger.setLevel(logging.INFO)

dictionary_logger.addHandler(vlh)
dictionary_logger.info("Initializing settings, logging to: %s" % logger_filename)
