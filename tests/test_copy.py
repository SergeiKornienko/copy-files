from copy_files.copy_files import get_path, prepare
# import tempfile
from os.path import join


XML = 'tests/fixtures/file.xml'
PATHS = {
    'file0': {
        'source_path': 'C:\\Windows\\system32',
        'destination_path': 'C:\\Program files',
        'file_name': 'kernel32.dll',
    },
    'file1': {
        'source_path': '/var/log',
        'destination_path': '/etc',
        'file_name': 'server.log',
    },
}
PATHS_FILE= {
    'source_path': '/var/log',
    'destination_path': '/etc',
    'file_name': 'server.log',
}
SRC_FILE = '/var/log/server.log'
DST_FILE = '/etc'


# def test_download_file():
#     with open(HTML) as infile:
#         html_input = infile.read()
#     with open(EXPECT_HTML) as infile:
#         html_expected = infile.read()
#     with open(IMG, 'rb') as infile:
#         img = infile.read()
#     with tempfile.TemporaryDirectory() as direct:
#         with requests_mock.Mocker() as mock:
#             mock.get(URL, text=html_input)
#             mock.get(URL_IMG, content=img)
#             mock.get(URL_JS, text='test')
#             mock.get(URL_CSS, text='test')
#             path_html = copy(URL, dir_for_save=direct)
#         with open(join(direct, NAME_DIR, NAME_IMG), 'rb') as infile:
#             assert infile.read() == img
#         with open(join(direct, NAME_DIR, NAME_JS), 'r') as infile:
#             assert infile.read() == 'test'
#         with open(join(direct, NAME_DIR, NAME_CSS), 'r') as infile:
#             assert infile.read() == 'test'
#         assert path_html == join(direct, NAME_HTML)
#         with open(path_html) as infile:
#             assert infile.read() == html_expected


def test_prepare():
    with open(XML) as infile:
        xml_input = infile.read()
    assert PATHS == prepare(xml_input)


def test_get_path():
    assert get_path(PATHS_FILE) == (SRC_FILE, DST_FILE)
#
# def test_http():
#     with pytest.raises(exceptions.RequestException):
#         with requests_mock.Mocker() as mock:
#             mock.get(URL, status_code=404)
#             copy(URL)
#
#
# def test_os():
#     with pytest.raises(OSError):
#         with requests_mock.Mocker() as mock:
#             mock.get(URL, text='test')
#             copy(URL, dir_for_save='/')
#
#
# def test_url_is_local():
#     assert is_local(URL_CSS, URL) is True
#     assert is_local('https://cdn2.hexlet.io/assets/menu.css', URL) is False
#
#
# def test_parse():
#
#
#
