#!/usr/bin/env python
import sys
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import os
import imp

config = None
s3conn = None

BASEDIR = os.path.abspath(os.path.realpath(__file__))
DEF_CONFIG_PATH = os.path.join(BASEDIR, 'config_local.py')


def load_config(path):
    """
    """
    global config
    config = imp.load_module('.', path)
    return config


def get_s3_key(remote_path):
    """
    Checks status of s3 archive.
    """
    bucket = s3conn.create_bucket(config.ORG_BUCKET)
    key = Key(bucket)
    key.key = remote_path
    return key


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote-path", required=True, type=str)
    parser.add_argument('--config', default=DEF_CONFIG_PATH, type=str)
    args = parser.parse_args()
    load_config(args.config)

    s3conn = S3Connection(
        config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_KEY)

    key = get_s3_key(args.remote_path)
    if key.exists():
        print "Archived"
        sys.exit(0)
    else:
        print "Not_Found"
        sys.exit(0)
    sys.exit(1)
