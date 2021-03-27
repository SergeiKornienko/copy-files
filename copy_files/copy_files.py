from os.path import join
from shutil import copy as copy_file
from progress.bar import Bar
import logging
from xml.etree import ElementTree


def copy(path_to_config):
    paths = prepare(open_file(path_to_config))
    for path in paths.values():
        (src, dst) = get_path(path)
        with Bar(
                f"{'Copy '}{src[:70]}{' to '}{dst[:70]}{': '}",
                max=len(paths) / 100,
                suffix='%(percent)d%%') as bar_file:
            try:
                copy_file(src, dst)
                bar_file.next()
            except OSError as error:
                logging.warning('Error copy of file: {a}'.format(a=error))
                bar_file.next()


def get_path(paths):
    return (
        join(paths['source_path'], paths['file_name']),
        paths['destination_path'],
    )


def open_file(path):
    with open(path, 'r') as infile:
        return infile.read()


def prepare(content_xml):
    root = ElementTree.fromstring(content_xml)
    paths = {}
    for i, child in enumerate(root):
        paths[child.tag + str(i)] = child.attrib
    return paths
