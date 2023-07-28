'''
Author : Iraqi Shadow or Iraqi Warrior
Channel: t.me/Babyl0n_Team
Contact: @Iraqi_Shadow
website: saveiraq.github.io
version: 1.0

'''


import requests
from colorama import Fore, init
import signal
import sys
from fake_useragent import UserAgent
import os


def sigint_handler(signal, frame):
    print ('\n\nFollow me on Telegram:@Babyl0n_Team')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

os.system("pip install fake_useragent")

init()

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def check_admin_page(url, retry_attempts=3):
    for _ in range(retry_attempts):
        headers = {
            "User-Agent": get_random_user_agent()
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"{Fore.GREEN}Admin page found: {url}")
                return
            else:
                print(f"{Fore.RED}False admin page: {url}")
                return
        except requests.exceptions.RequestException as e:
            print(f"{Fore.YELLOW}Request failed: {e}")
            continue

def search_admin_pages(base_url, wordlist):
    with open(wordlist, "r") as file:
        admin_pages = file.read().splitlines()

    for admin_page in admin_pages:
        url = f"{base_url}/{admin_page}"
        check_admin_page(url)

def main():
    uurl = input("Enter the URL (with http/https): ")
    wordlistt = "wordlist.txt"
    search_admin_pages(uurl, wordlistt)

if __name__ == "__main__":
    main()
