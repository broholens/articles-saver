import os
from util import browser_util, file_util
from config.config import IMG_DIR


class Article:
    def __init__(self):
        self.browser = browser_util.make_browser()

    def save(self, url):
        self.browser.get(url)
        article = browser_util.html2article(self.browser.page_source)
        img_filename = file_util.url2filename(self.browser.current_url)
        img_path = os.path.join(IMG_DIR, img_filename)
        self.save_img(img_path)
        return {
            'url': self.browser.current_url,
            'article': article,
            'img_path': img_path
        }

    def save_img(self, img_path):
        scroll_width = self.browser.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = self.browser.execute_script('return document.body.parentNode.scrollHeight')
        self.browser.set_window_size(scroll_width, scroll_height)
        self.browser.save_screenshot(img_path)
