import pytest
import json
import requests
import os
from dotenv import load_dotenv
import utils

load_dotenv()
with open(os.environ.get("INFOPATH"), "r") as f:
    info = json.load(f)
url = info["urls"]["url_api_brew"]


def test_all_brews(build_link_all_brews):
    res = requests.get(build_link_all_brews)
    brews = res.json()
    brews_names = [brew['name'] for brew in brews]
    brews_cities = [brew['city'] for brew in brews]
    brews_countries = [brew['country'] for brew in brews]
    assert res.status_code == 200, "Status code differ from 200"
    assert len(brews) == len(set([brew["id"] for brew in brews])), "Doubles in response"
    assert None not in brews_names, "Some name is None"
    assert None not in brews_cities, "Some city is None"
    assert None not in brews_countries, "Some country is None"


@pytest.mark.parametrize("city", [utils.rnd_city() for i in range(3)])
def test_all_brews_filter(city, build_link_all_brews):
    city_url = city.lower().replace(" ", "_")
    res = requests.get(utils.build_link(build_link_all_brews, f"?by_city={city_url}"))
    assert res.status_code == 200, "Status code differ from 200"
    els = res.json()
    assert len(els) == len(set([el["id"] for el in els])), "Doubles in response"
    assert all((city.lower() in brew.get('city').lower() for brew in els)), "Wrong city in the filter result"


@pytest.mark.parametrize("id", [utils.rnd_id() for i in range(3)])
def test_get_brew(id, build_link_all_brews):
    res = requests.get(utils.build_link(build_link_all_brews, f"/{id}"))
    brew = res.json()
    assert res.status_code == 200, "Status code differ from 200"
    assert isinstance(brew, dict), "There are same ids for several objects"
    assert brew.get("name") is not None, "Name is None"
    assert brew.get("city") is not None, "City is None"
    assert brew.get("country") is not None, "Country is None"


@pytest.mark.parametrize("id", [utils.rnd_uuid() for i in range(3)])
def test_get_brew_negative(id, build_link_all_brews):
    res = requests.get(utils.build_link(build_link_all_brews, f"/{id}"))
    assert res.status_code == 404, "Status code differ from 404"
    assert "<title>Not Found</title>" in str(res.content), (
        "No information about error on the page"
    )
    assert "<!DOCTYPE html>" in str(res.content), "No html file in response"


@pytest.mark.parametrize("amnt, expected", [(1, 1), (25, 25), (50, 50)])
def test_get_random_brew(amnt, expected, build_link_all_brews):
    res = requests.get(utils.build_link(build_link_all_brews, f"/random?size={amnt}"))
    brews = res.json()
    assert res.status_code == 200, f"Status code is not 200 for {amnt} breweries"
    assert len(brews) == expected, f"Amount of breweries doesnt equal to {amnt}"
    assert len(brews) == len(set(map(lambda x: x["id"], brews))), (
        "There are doubles in the list"
    )
    assert brews[utils.rnd_el(brews)]["name"] is not None, "Name is None"
    assert brews[utils.rnd_el(brews)]["city"] is not None, "City is None"
    assert brews[utils.rnd_el(brews)]["country"] is not None, "Country is None"
