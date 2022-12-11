import os
import re
from urllib.parse import urlparse


def generate_filename(url):
    parsed = urlparse(url)
    file_name = parsed.netloc + os.path.splitext(parsed.path)[0]
    result_name = re.sub(r'\W', '-', file_name) + '.html'
    return result_name


def generate_content_filename(url, path, ext):
    parsed = urlparse(url)
    file_name = parsed.netloc + '-' + path
    result_name = re.sub(r'\W', '-', file_name) + ext
    return result_name
