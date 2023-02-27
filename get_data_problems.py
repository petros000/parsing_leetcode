from selenium import webdriver
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def get_html(url):
    useragent = UserAgent()

    options_browser = webdriver.ChromeOptions()
    options_browser.add_argument(f"user-agent={useragent.random}")

    browser = webdriver.Chrome(
        executable_path=f"drivers/chromedriver.exe",
        options=options_browser
    )

    try:
        browser.get(url=url)
        src_html = browser.page_source
        time.sleep(5)
        return src_html

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()


def data_all_problems():
    data = dict()
    count = 0
    for page in range(1, 2):
        url_page = f"https://leetcode.com/problemset/all/?page={page}"
        page_html = get_html(url_page)
        soup = BeautifulSoup(page_html, "lxml")
        tasks = soup.find_all(class_=['h-5', 'hover'])
        for task in tasks:
            link = task.find("a").get("href")
            print(link)
    return tasks


# url = "https://habr.com/ru/post/444460/"
# html = get_html(url)
tasks = data_all_problems()
print(tasks)
