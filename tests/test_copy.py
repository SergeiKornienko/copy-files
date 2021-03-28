from copy_files.copy_files import copy, prepare
import os
import glob
import pytest
from xml.etree import ElementTree
from shutil import rmtree

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
    os.mkdir('tests/fixtures/4/')
    os.mkdir('tests/fixtures/5/')
    copy('tests/fixtures/config.xml')
    with open('tests/fixtures/1/Krug S. Круг С. - Не заставляйте меня думать', 'rb') as infile:  # noqa: E501
        file1 = infile.read()
    with open('tests/fixtures/4/Krug S. Круг С. - Не заставляйте меня думать', 'rb') as infile:  # noqa: E501
        file4 = infile.read()
    assert file1 == file4
    with open('tests/fixtures/2/Операционная система Unix (Робачевский, 2003).djvu', 'rb') as infile:  # noqa: E501
        file2 = infile.read()
    with open('tests/fixtures/5/Операционная система Unix (Робачевский, 2003).djvu', 'rb') as infile:  # noqa: E501
        file5 = infile.read()
    assert file2 == file5
    rmtree('tests/fixtures/4/')
    rmtree('tests/fixtures/5/')



def test_prepare():
    with open(XML) as infile:
        xml_input = infile.read()
    assert PATHS == prepare(xml_input)


def test_copy_exception():
    with pytest.raises(OSError):
        copy('tests/fixtures/config3.xml')
    with pytest.raises(ElementTree.ParseError):
        copy('tests/fixtures/config4.xml')
