#!/usr/bin/env python
import argparse
import os

from enumerate_iam.main import enumerate_iam


def main():
    parser = argparse.ArgumentParser(description='Enumerate IAM permissions')

    parser.add_argument('--access-key', help='AWS access key', required=False, default=None)
    parser.add_argument('--secret-key', help='AWS secret key', required=False, default=None)
    parser.add_argument('--session-token', help='STS session token', required=False, default=None)
    parser.add_argument('--region', help='AWS region to send API requests to', default='us-east-1')

    args = parser.parse_args()

    if "AWS_ACCESS_KEY_ID" in os.environ:
        access_key = os.environ.get("AWS_ACCESS_KEY_ID")
    else:
        access_key = args.access_key

    if "AWS_SECRET_ACCESS_KEY" in os.environ:
        secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    else:
        secret_key = args.secret_key

    if "AWS_SESSION_TOKEN" in os.environ:
        session_token = os.environ.get("AWS_SESSION_TOKEN")
    else:
        session_token = args.session_token

    if "AWS_REGION" in os.environ:
        region = os.environ
    else:
        region = args.region

    enumerate_iam(access_key,
                  secret_key,
                  session_token,
                  region)


if __name__ == '__main__':
    main()
