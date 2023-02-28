import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import json


def get_html(url):
    useragent = UserAgent()

    options_browser = webdriver.ChromeOptions()
    options_browser.add_argument(f"user-agent={useragent.chrome}")

    browser = webdriver.Chrome(
        executable_path=f"drivers/chromedriver.exe",
        options=options_browser
    )

    try:
        browser.get(url=url)
        time.sleep(6)
        src_html = browser.page_source

        return src_html

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()


def data_all_problems():
    data = dict()
    count = 0
    for page in range(1, 53):
        url_page = f"https://leetcode.com/problemset/all/?page={page}"
        page_html = get_html(url_page)
        soup = BeautifulSoup(page_html, "lxml")
        tasks = soup.find_all(class_="odd:bg-layer-1 even:bg-overlay-1 dark:odd:bg-dark-layer-bg dark:even:bg-dark-fill-4")

        for task in tasks:
            if count == 0:
                count += 1
                continue

            is_prem = True if task.find("svg", class_="ml-2 shrink-0") else False

            name = task.find(class_=['h-5']).text
            link = "https://leetcode.com" + task.find("a").get("href")

            data[str(count)] = {
                "name": name,
                "is_premium": is_prem,
                "link": link,
            }
            count += 1
        time.sleep(random.randrange(2, 5))

    return data


# url = "https://habr.com/ru/post/444460/"
# html = get_html(url)
def main():
    data = data_all_problems()
    print(len(data))
    with open('links_to_tasks.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()






