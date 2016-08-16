import os

BASEDIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
DEF_CONFIG_PATH = os.path.join(BASEDIR, 'config_local.py')

if not os.path.exists(DEF_CONFIG_PATH):
    """
    For quick start set to config_example if user did not yet
    setup config_local.py
    """
    DEF_CONFIG_PATH = os.path.join(BASEDIR, 'config_example.py')

config = None


def load_config(path):
    """
    """
    import imp
    global config
    config = imp.load_source('', path)
    return config
