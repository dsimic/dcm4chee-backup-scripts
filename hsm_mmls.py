#!/usr/bin/env python
import sys
from boto.s3.key import Key
from boto.s3.connection import S3Connection

AWS_ACCESS_KEY_ID = "YOUR_KEY_ID"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"
ORG_BUCKET = 'YOUR_BUCKET'

s3conn = S3Connection(
    AWS_ACCESS_KEY_ID, AWS_SECRET_KEY)


def get_s3_key(remote_path):
    """
    Checks status of s3 archive.
    """
    bucket = s3conn.create_bucket(ORG_BUCKET)
    key = Key(bucket)
    key.key = remote_path
    return key


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote-path", required=True, type=str)
    args = parser.parse_args()
    key = get_s3_key(args.remote_path)
    if key.exists():
        print "Archived"
        sys.exit(0)
    else:
        print "Not_Found"
        sys.exit(0)
    sys.exit(1)
