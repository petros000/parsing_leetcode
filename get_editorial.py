from get_data_problems import get_html
from bs4 import BeautifulSoup


def is_solution_unlock(tag):
    if tag:
        return True
    return False


def get_editorial_solution():
    pass


def get_data_editorial(url):
    url_page = url + "editorial/"

    data_editorial = dict()

    page_html = get_html(url_page)

    soup = BeautifulSoup(page_html, "lxml")
    tag_unlock = soup.find("a", string="Subscribe")

    if is_solution_unlock(tag_unlock):
        data_editorial["editorial solution"] = "unlock"
    else:
        if soup.find("div", class_="flex h-full w-full overflow-y-auto") is None:
            data_editorial["editorial solution"] = None
        else:
            get_editorial_solution()


url1 = "https://leetcode.com/problems/triangle/"
url2 = "https://leetcode.com/problems/text-justification/"
get_data_editorial(url1)
