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


def get_data_solutions_page(url):
    page_html = get_html(url)
    soup = BeautifulSoup(page_html, "lxml")


size = get_size_page("https://leetcode.com/problems/two-sum/")
print(size)
