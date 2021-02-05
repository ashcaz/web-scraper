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
    if not validators.url(url):
        raise Exception("Not a valid URL, Try again")
    else:
        print("URL is valid")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("a", text="citation needed")

    return result


def get_citations_needed_count(scraped_results):

    citations_needed = len(scraped_results)

    return citations_needed


def get_citations_needed_report(scraped_results):

    for citation in scraped_results:

        text = citation.find_parent("p").text
        print(text)


# if __name__ == '__main__':
