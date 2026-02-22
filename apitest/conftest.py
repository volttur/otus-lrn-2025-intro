import pytest
from dotenv import load_dotenv
import os
import json
import utils

load_dotenv()
with open(os.environ.get("INFOPATH"), "r") as f:
    info = json.load(f)
url = info["urls"]["url_api"]
url_brew = info["urls"]["url_api_brew"]
url_json = info["urls"]["url_api_json"]


@pytest.fixture
def build_link_rnd():
    return utils.build_link(url, "/breeds/image/random")


@pytest.fixture
def build_link_all_breeds():
    return utils.build_link(url, "/breeds/list/all")


@pytest.fixture
def build_link_breed():
    return utils.build_link(url, "/breed")


@pytest.fixture
def build_link_all_brews():
    return utils.build_link(url_brew, "/breweries")


@pytest.fixture
def build_link_all_posts():
    return utils.build_link(url_json, "/posts")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="Setting up url for the test",
    )
    parser.addoption(
        "--status_code",
        action="store",
        default="200",
        help="Setting up status code for the test",
    )


@pytest.fixture
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def get_status_code(request):
    return request.config.getoption("--status_code")
