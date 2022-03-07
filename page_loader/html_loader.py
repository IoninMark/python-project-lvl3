import os
import requests
from page_loader.filename_generator import generate_filename


def download(url, dir_path, client=requests):
    r = client.get(url)  # allow_redirects=True
    name = generate_filename(url)
    file_path = os.path.join(dir_path, name)
    with open(file_path, 'w') as file:
        file.write(r.text)
    return file_path
