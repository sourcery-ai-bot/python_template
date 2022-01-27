#!/usr/bin/env python3

# import argparse
# import numpy as np
# import os
import pandas as pd
import re
import requests
import requests_cache
from bs4 import BeautifulSoup, Comment
from datetime import timedelta
# from decouple import config
# from icecream import ic
from pathlib import Path
# from playwright.async_api import async_playwright
# from playwright.sync_api import sync_playwright
# from prettytable import PrettyTable
# from requests_cache import CachedSession

"""
The commented out section is boilerplate for common operations.
Feel free to uncomment and/or delete after first commit.
"""
## env
# home = os.path.expandvars("$HOME")
# now = datetime.datetime.now()
# out = f"{home}/Downloads/result_{now:%Y%m%d_%H%M%S}.csv"
# env = Path('/.env')

## pwd
# cwd = os.path.dirname(os.path.abspath("__file__"))
# # print(f"Current working directory: {cwd}")

# dir_path = os.path.dirname(os.path.realpath(__file__))
# # print(f"File directory: {dir_path}")

# if cwd != dir_path:
#     os.chdir(dir_path)
#     print(os.getcwd())

# folders = ['logs', 'user_data']

# for folder in folders:
#     if not Path(folder).exists():
#         os.mkdir(os.path.join(cwd, folder))

# # creds
# if env.exists():
#     HOST = config('HOST', default='localhost')
#     USER = config('USER')
#     PASS = config('PASS')
# else:
#     HOST = os.getenv('HOST', default='localhost')
#     USER = os.getenv('USER')
#     PASS = os.getenv('PASS')

## mkdir -p ./csv && cd $_
# if Path('csv').exists():
#     os.chdir('./csv')
#     print("Changed to the folder: " + os.getcwd())
# else:
#     try:
#         os.makedirs('./csv')
#     except FileExistsError as exists:
#         print('Folder already exists')
#     finally:
#         os.chdir('./csv')
#         print("Changed to the folder: " + os.getcwd())

base_url = 'https://app.cloud-logon.com/dev/'
calc_url = base_url + "calculator"
hint_url = base_url + "easy_mode"

requests_cache.install_cache("api_cache")

main_page = requests.get(calc_url)

page_soup = BeautifulSoup(main_page.text, 'html.parser')
print(f"MAIN PAGE\n{page_soup}")

comments = page_soup.find_all(string=lambda text: isinstance(text, Comment))
print("COMMENTS")
for comment in comments:
    print(comment.strip())

comment_regex = re.compile(r'\d{12}')
raw = comment_regex.search(str(comments))
aws_account_number = raw.group(0)
print(f"AWS ACCOUNT NUMBER: {aws_account_number}")

# TODO: missing auth token
hint_page = requests.get(hint_url)
hint_page_soup = BeautifulSoup(hint_page.text, 'html.parser')
print(f"\nHINT PAGE\n{hint_page_soup}")
print(hint_page.text)
