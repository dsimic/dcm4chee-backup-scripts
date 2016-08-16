#!/usr/bin/env python
import os
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import imp

config = None
s3conn = None

BASEDIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))


def load_common():
    common = imp.load_source('', os.path.join(BASEDIR, 'common.py'))
    return common

common = load_common()


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
    parser.add_argument('--dest', type=str, help='AWS S3 object key')
    parser.add_argument(
        '--config', default=common.DEF_CONFIG_PATH, type=str,
        help='Path to config containing AWS auth info, default is %s' %
        common.DEF_CONFIG_PATH
    )
    args = parser.parse_args()

    common.load_config(args.config)
    config = common.config

    s3conn = S3Connection(
        config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_KEY)

    copy_file_to_s3(args.in_tar, args.dest)
