from get_data_problems import get_html
from bs4 import BeautifulSoup
import re


def get_description_info(tag_info, data_description):
    [difficulty, likes, dislakes] = tag_info.get_text(separator=" ").split()
    data_description["info"] = {
                                "difficulty": difficulty,
                                "likes": likes,
                                "dislakes": dislakes
                                }


def get_formulation_problem(tag_problem, data_description):
    full_text = tag_problem.get_text(separator=" ")
    data_description['problem'] = full_text


def get_related_topics(tag_topics, data_description):
    topics = tag_topics.find_all("a")
    data_description["related topics"] = [topic.text for topic in topics]


def get_data_description(url):
    url_page = url + "description/"

    data_description = dict()

    page_html = get_html(url_page)

    soup = BeautifulSoup(page_html, "lxml")

    tag_info = soup.find("div", class_="mt-3 flex space-x-4")
    tag_problem = soup.find("div", class_="px-5 pt-4")
    tag_topics = soup.find(class_="mt-2 flex flex-wrap gap-y-3")

    get_description_info(tag_info, data_description)
    get_formulation_problem(tag_problem, data_description)
    get_related_topics(tag_topics, data_description)

    return data_description


url = "https://leetcode.com/problems/two-sum/"
print(get_data_description(url))
