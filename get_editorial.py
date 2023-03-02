from get_data_problems import get_html
from bs4 import BeautifulSoup


def get_editorial_solution(soup):
    data_solution = dict()
    tag_class = soup.find(class_="_16yfq _2YoR3")
    contents = tag_class.contents
    for content in contents:
        if content.name == "h4":
            cur_h4 = content.text
            data_solution[cur_h4] = dict()

        if content.name == "p":
            if content.contents[0].name == "strong":
                cur_strong = content.text
                data_solution[cur_h4][cur_strong] = ""
            else:
                data_solution[cur_h4][cur_strong] += content.text

    print(data_solution)





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

        get_editorial_solution(tag_edit_solutions)


url1 = "https://leetcode.com/problems/triangle/"
url2 = "https://leetcode.com/problems/text-justification/"
url3 = "https://leetcode.com/problems/two-sum/"
get_data_editorial(url3)
