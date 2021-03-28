"""Function for launch cli-module."""
import argparse
import pathlib

DESCRIPTION = 'application for copying files according to the config file'


def get_args():
    """Launch cli-module."""
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
    )
    parser.add_argument(
        'path', type=pathlib.Path, help='path to the config file',
    )
    parser.add_argument(
        '-l', '--loglevel',
        default=0,
        type=int,
        help='''
            Set level logging:
            0: logging.WARNING
            1: logging.INFO
            2: logging.DEBUG
            '''
    )
    args = parser.parse_args()
    path = args.path
    log = args.loglevel
    return path, log
