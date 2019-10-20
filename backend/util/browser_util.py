from selenium import webdriver
from newspaper import fulltext


def make_browser():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"')
    browser = webdriver.Chrome(chrome_options=opts)
    browser.maximize_window()
    return browser


def html2article(html):
    return fulltext(html)
