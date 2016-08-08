#!/usr/bin/env python

from boto.s3.key import Key
from boto.s3.connection import S3Connection

AWS_ACCESS_KEY_ID = "YOUR_KEY_ID"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"
ORG_BUCKET = 'YOUR_BUCKET'

s3conn = S3Connection(
    AWS_ACCESS_KEY_ID, AWS_SECRET_KEY)


def copy_file_to_s3(inpath, remote_path):
    """
    Copies file to regulsr s3 storage.
    """
    bucket = s3conn.create_bucket(ORG_BUCKET)
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
    args = parser.parse_args()
    copy_file_to_s3(args.in_tar, args.dest)
