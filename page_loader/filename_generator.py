import os
import re
from urllib.parse import urlparse


def generate_filename(url):
    parsed = urlparse(url)
    file_name = parsed.netloc + os.path.splitext(parsed.path)[0]
    result_name = re.sub('\W', '-', file_name) + '.html'
    return result_name


# res = generate_filename('https://www.google.ru/sea3rc$h/tt3Wcsct.html')
# print(res)