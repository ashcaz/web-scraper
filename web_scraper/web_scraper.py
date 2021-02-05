import requests
from bs4 import BeautifulSoup
import validators

# url = "https://en.wikipedia.org/wiki/History_of_Haiti"

# response = requests.get(url)

# content = response.content

# # print(content)

# soup = BeautifulSoup(content, "html.parser")
# result = soup.find_all("a", text="citation needed")
# print(result)
# print(len(result))


def scraped_results(url):
    pass


def get_citations_needed_count(url):

    if not validators.url(url):
        raise Exception("Not a valid URL, Try again")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("a", text="citation needed")
    citations_needed = len(result)
    return citations_needed
