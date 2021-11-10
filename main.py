#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from Search import Search

yandex = 'https://yandex.ru'
google = 'https://www.google.com'

count_deep_seek_page = 4
current_website = 'http://obivshik.ru'

key_word = 'купить велосипед'


def start_bot():
    driver = webdriver
    search_class = Search(
        url=yandex, driver=driver,
        key_word=key_word,
        count_deep_seek_page=count_deep_seek_page,
        current_website=current_website
    )
    search_class.set_options_and_fake_agent()
    search_class.go_to_search_page()
    all_websites = search_class.find_all_websites()
    search_class.check_current_websites(all_websites)
    search_class.behavioral_factor()


if __name__ == '__main__':
    start_bot()
