import pytest
import validators
from web_scraper.web_scraper import (
    get_citations_needed_count,
    scraped_results,
    get_citations_needed_report,
)
from web_scraper import __version__


def test_version():
    assert __version__ == "0.1.0"


# @pytest.mark.skip("pending")
def test_scraped_results_bad_url():
    with pytest.raises(Exception) as err:
        scraped_results("https://badurl")

        assert str(err.value) == "Not a valid URL, Try again"


# @pytest.mark.skip("pending")
def test_scraped_results_good_url(capsys):
    scraped_results("https://en.wikipedia.org/wiki/History_of_Haiti")
    captured = capsys.readouterr()
    assert captured.out == "URL is valid\n"
