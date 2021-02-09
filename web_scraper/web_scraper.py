import requests
from bs4 import BeautifulSoup
import validators

url = "https://en.wikipedia.org/wiki/History_of_Haiti"

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

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("a", text="citation needed")

    return result


def get_citations_needed_count(scraped_results):

    citations_needed = len(scraped_results)

    return citations_needed


def get_citations_needed_report(scraped_results):

    report_list = []

    for citation in scraped_results:

        text = citation.find_parent("p").text
        report_list.append(text)

    return "\n\n".join(report_list)


if __name__ == "__main__":

    scraped_info = scraped_results(url)

    count = get_citations_needed_count(scraped_info)

    report = get_citations_needed_report(scraped_info)

    print(f"\nCitations Count: {count} \n\nCitations Report:\n\n{report} ")
