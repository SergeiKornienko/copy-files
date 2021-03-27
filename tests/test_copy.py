from copy_files.copy_files import copy, get_path, prepare
import os
import glob
# import tempfile
# from os.path import join


XML = 'tests/fixtures/file.xml'
PATHS = [
    {
        'source_path': 'C:\\Windows\\system32',
        'destination_path': 'C:\\Program files',
        'file_name': 'kernel32.dll',
    },
    {
        'source_path': '/var/log',
        'destination_path': '/etc',
        'file_name': 'server.log',
    },
]
PATHS_FILE = {
    'source_path': '/var/log',
    'destination_path': '/etc',
    'file_name': 'server.log',
}
SRC_FILE = '/var/log/server.log'
DST_FILE = '/etc'


def test_copy():
    files4 = glob.glob('tests/fixtures/4/*')
    for f in files4:
        os.remove(f)
    files5 = glob.glob('tests/fixtures/5/*')
    for f in files5:
        os.remove(f)
    files6 = glob.glob('tests/fixtures/6/*')
    for f in files6:
        os.remove(f)
    print(os.getcwd())
    copy('tests/fixtures/config.xml')


def test_prepare():
    with open(XML) as infile:
        xml_input = infile.read()
    assert PATHS == prepare(xml_input)


def test_get_path():
    assert get_path(PATHS_FILE) == (SRC_FILE, DST_FILE)
