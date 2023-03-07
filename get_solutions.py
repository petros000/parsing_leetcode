from bs4 import BeautifulSoup
import json
from selenium import webdriver
from fake_useragent import UserAgent
import time
from selenium.webdriver.common.by import By
from get_data_problems import get_html


def get_size_page(url):
    page_html = get_html(url + "solutions/?orderBy=most_votes")
    soup = BeautifulSoup(page_html, "lxml")
    navigation = soup.find_all("nav")
    sizes = navigation[1].find_all("button")

    return int(sizes[-2].string)


def get_info_data_user_solution(tag):
    info_data = dict()
    name_sol = tag.find("span").string
    link_sol = tag.find("a").get("href")
    user_name = tag.find(class_="flex items-center gap-5").find("a").string
    date_sol = tag.find(class_="flex items-center gap-1.5").find("span").string
    info_data["name_sol"] = name_sol
    info_data["link_sol"] = link_sol
    info_data["user_name"] = user_name
    info_data["date_sol"] = date_sol

    return info_data


def get_data_solutions_page(url):
    url_page = url + "solutions/?orderBy=most_votes&page="
    max_size_page = get_size_page(url)
    data = dict()
    print(max_size_page)
    user_count = 1
    for page in range(1, 3):
        url_page_sol = url_page + f"{page}"
        page_html = get_html(url_page_sol)
        soup = BeautifulSoup(page_html, "lxml")
        user_solutions = soup.find_all(class_="flex w-full flex-col gap-1 overflow-hidden")
        for user_solution in user_solutions:
            data[str(user_count)] = get_info_data_user_solution(user_solution)
            user_count += 1

    return data


# size = get_size_page("https://leetcode.com/problems/two-sum/")
# print(size)
# "https://leetcode.com/problems/two-sum/solutions/?orderBy=most_votes&page=2"
url = "https://leetcode.com/problems/two-sum/"
res = get_data_solutions_page(url)
print(res)
