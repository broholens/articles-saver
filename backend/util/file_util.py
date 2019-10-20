import os
import base64


def url2filename(url):
    return base64.urlsafe_b64encode(url.encode()).decode() + '.png'


def filename2url(filename):
    return base64.urlsafe_b64decode(filename.strip('.png').encode()).decode()
