#!/usr/bin/env python

from boto.s3.key import Key
from boto.s3.connection import S3Connection
import imp

config = None

BASEDIR = os.path.abspath(os.path.realpath(__file__))
DEF_CONFIG_PATH = os.path.join(BASEDIR, 'config_local.py')


def load_config(path):
    """
    """
    global config
    config = imp.load_module('.', path)


def copy_file_to_s3(inpath, remote_path):
    """
    Copies file to regulsr s3 storage.
    """
    bucket = s3conn.create_bucket(config.ORG_BUCKET)
    key = Key(bucket)
    key.key = remote_path
    key.set_contents_from_filename(inpath)
    # print key.etag
    return key


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--in-tar", required=True, type=str)
    parser.add_argument('--dest', type=str)
    parser.add_argument('--config', default=DEF_CONFIG_PATH, type=str)
    args = parser.parse_args()

    load_config(args.config)

    s3conn = S3Connection(
        config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_KEY)

    copy_file_to_s3(args.in_tar, args.dest)
