from get_data_problems import get_html
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from fake_useragent import UserAgent
import time
from selenium.webdriver.common.by import By


def get_code(url):
    data_code = dict()

    useragent = UserAgent()

    options_browser = webdriver.ChromeOptions()
    options_browser.add_argument(f"user-agent={useragent.chrome}")

    browser = webdriver.Chrome(
        executable_path=f"C:/Users/ppp/chromedriver.exe",
        options=options_browser
    )

    try:
        browser.get(url=url)
        page_html = browser.page_source
        time.sleep(1)
        element = browser.find_element(By.CLASS_NAME, "lang-btn-set")

        buttons = element.find_elements(By.TAG_NAME, 'button')

        for b in buttons:
            b.click()
            soup = BeautifulSoup(page_html, "lxml")
            code = soup.find("textarea")
            data_code[b.text] = code.string
            time.sleep(2)

        return data_code

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()


def get_editorial_solution(soup):
    data_solution = dict()
    tag_class = soup.find(class_="_16yfq _2YoR3")
    contents = tag_class.contents
    for content in contents:
        if content.name == "h4":
            cur_tag_h4 = content.text
            data_solution[cur_tag_h4] = dict()

        if content.name == "p":
            if content.contents[0].name == "strong":
                cur_strong = content.text
                data_solution[cur_tag_h4][cur_strong] = []
            else:
                data_solution[cur_tag_h4][cur_strong].append(content.text)

        if content.name == "iframe":
            url = content.get("src")
            data_solution[cur_tag_h4]["Implementation"] = get_code(url)

    return data_solution


def get_data_editorial(url):
    url_page = url + "editorial/"

    data_editorial = dict()

    page_html = get_html(url_page)

    soup = BeautifulSoup(page_html, "lxml")

    is_solution_unlock = True if soup.find("h4") is None else False

    if is_solution_unlock:
        data_editorial["editorial solution"] = None

    else:
        tag_edit_solutions = soup.find("div", class_="flex w-full flex-col gap-4 px-5 pb-8 pt-0")

        data_editorial["editorial solution"] = get_editorial_solution(tag_edit_solutions)

    return data_editorial


url1 = "https://leetcode.com/problems/triangle/"
url2 = "https://leetcode.com/problems/text-justification/"
url3 = "https://leetcode.com/problems/two-sum/"
data = get_data_editorial(url3)
print(json.dumps(data, indent=5))

# cods = get_code("https://leetcode.com/playground/cvvgJGBX/shared")
# print(cods)
