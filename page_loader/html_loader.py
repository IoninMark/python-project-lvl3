import os
import requests
import sys
from bs4 import BeautifulSoup
from page_loader.filename_generator import generate_filename
from page_loader.filename_generator import generate_content_filename
from urllib.parse import urljoin


def download(url, dir_path, client=requests):
    response = client.get(url)  # allow_redirects=True
    soup = BeautifulSoup(response.text, "html.parser")
    name = generate_filename(url)
    content_dir_name = os.path.splitext(name)[0] + '_files'
    content_path = os.path.join(dir_path, content_dir_name)
    file_path = os.path.join(dir_path, name)
    tags = {'img': 'src'}  # , 'link': 'href', 'script': 'src'}
    for tag, inner in tags.items():
        save_content(soup, content_path, client, url, tag, inner)
    with open(file_path, 'w') as file:
        file.write(soup.prettify())
    return file_path


def save_content(soup, content_folder, client, url, tag, inner):
    if not os.path.exists(content_folder):
        os.mkdir(content_folder)
    for items in soup.findAll(tag):
        if items.has_attr(inner):
            try:
                filename, ext = os.path.splitext(items[inner])
                filename = generate_content_filename(url, filename, ext)
                file_url = urljoin(url, items.get(inner))
                filepath = os.path.join(content_folder, filename)
                content_dir = os.path.basename(content_folder)
                items[inner] = os.path.join(content_dir, filename)
                if not os.path.isfile(filepath):
                    with open(filepath, 'wb') as file:
                        file_bin = client.get(file_url)
                        file.write(file_bin.content)
            except Exception as exc:
                print(exc, file=sys.stderr)
