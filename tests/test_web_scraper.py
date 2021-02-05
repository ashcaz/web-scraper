import pytest
import validators
from web_scraper.web_scraper import get_citations_needed_count
from web_scraper import __version__


def test_version():
    assert __version__ == "0.1.0"


# @pytest.mark.skip("pending")
def test_get_citations_bad_url():
    with pytest.raises(Exception) as err:
        get_citations_needed_count("https://badurl")

        assert str(err.value) == "Not a valid URL, Try again"


def test_get_citations_good_url():
    actual = get_citations_needed_count(
        "https://en.wikipedia.org/wiki/History_of_Haiti"
    )
    expected = 3
    assert actual == expected
