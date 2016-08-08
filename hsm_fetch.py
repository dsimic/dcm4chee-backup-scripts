#!/usr/bin/env python
from boto.s3.key import Key
from boto.s3.connection import S3Connection

AWS_ACCESS_KEY_ID = "YOUR_KEY_ID"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"
ORG_BUCKET = 'YOUR_BUCKET'

s3conn = S3Connection(
    AWS_ACCESS_KEY_ID, AWS_SECRET_KEY)

ORG_BUCKET = 'mhc-dorada'


def fetch_from_s3(remote_path, dest_file):
    """
    Checks status of s3 archive.
    """
    bucket = s3conn.create_bucket(ORG_BUCKET)
    key = Key(bucket)
    key.key = remote_path
    key.get_contents_to_filename(dest_file)
    return key


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote-path", required=True, type=str)
    parser.add_argument("--dest", required=True, type=str)
    args = parser.parse_args()
    key = fetch_from_s3(args.remote_path, args.dest)
