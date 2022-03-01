import requests
from page_loader.filename_generator import generate_filename


def download(url, dir_path):
    r = requests.get(url, allow_redirects=True)
    file_name = generate_filename(url)
    with open(dir_path + '/test.html', 'wb') as file:
        file.write(r.content)
    return dir_path + '/' + file_name


# str = download('https://www.google.ru', '/Users/mark/Python/python-project-lvl3/tests')
# print(str)