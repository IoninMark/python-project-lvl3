import pook
import os
from page_loader.html_loader import download


class FakeClient:
    def __init__(self, data):
        self.text = data
        self.content = data

    def get(self, url):
        return self


def test_download(tmpdir):
    file_name = 'tests/fixtures/test_file.html'
    with open(file_name) as file:
        data = file.read()
    client = FakeClient(data)
    test_dir = tmpdir.mkdir("sub")
    file_path = download('https://www.test.ru', test_dir, client=client)
    with open(file_path) as new_file:
        new_data = new_file.read()
    assert new_data != data
    assert file_path == os.path.join(test_dir, 'www-test-ru.html')
    assert 'www-test-ru_files' in os.listdir(test_dir)
    assert 'www-test-ru-image.jpeg' in os.listdir(os.path.join(test_dir, 'www-test-ru_files'))


@pook.on
def test_download_http(tmpdir):
    pook.get(
        'https://www.google.com',
        reply=200,
        response_json='Nice'
    )
    test_dir = tmpdir.mkdir("sub")
    file_path = download('https://www.google.com', test_dir)
    with open(file_path) as new_file:
        new_data = new_file.read()
    assert new_data == 'Nice\n'
