import pytest
import json
import requests
import os
from dotenv import load_dotenv
import re
import utils

load_dotenv()
with open(os.environ.get("INFOPATH"), "r") as f:
    info = json.load(f)
stat_ok = info["statuses"]["pass"]
stat_err = info["statuses"]["fail"]
lim_up = info["data"]["rnd_limit_up"]
lim_bot = info["data"]["rnd_limit_bottom"]
url_img = info["urls"]["url_img"]
url_api = info["urls"]["url_api"]


def test_all_breeds(build_link_all_breeds):
    res = requests.get(build_link_all_breeds)
    breeds = res.json().get("message")
    assert res.status_code == 200, "Status code is not 200"
    assert res.json().get("status") == stat_ok, 'Status doesnt equal "success"'
    assert len(set(breeds)) == len(breeds), "List contains doubles"


@pytest.mark.parametrize("amount, expected", [(-1, lim_bot), (0, lim_bot), (51, lim_up)])
def test_random_edges_negative(amount, expected, build_link_rnd):
    res = requests.get(f"{build_link_rnd}/{amount}")
    assert res.status_code == 200, f"Status code is not 200 for {amount} imgs"
    imgs = res.json().get("message")
    assert res.json().get("status") == stat_ok, (
        f'Status for {amount} imgs doesnt equal to "success"'
    )
    assert len(imgs) == expected, f"Amount of images doesnt equal to {amount}"


@pytest.mark.parametrize("amount, expected", [(1, 1), (25, 25), (50, 50)])
def test_random_get_img(amount, expected, build_link_rnd):
    res = requests.get(f"{build_link_rnd}/{amount}")
    imgs = res.json().get("message")
    pattern = re.compile(rf"{url_img}[\d\w\-\/_.]*\.jpg", re.I)
    assert res.status_code == 200, f"Status code is not 200 for {amount} imgs"
    assert res.json().get("status") == stat_ok, (
        f'Status for {amount} imgs doesnt equal to "success"'
    )
    assert len(imgs) == expected, f"Amount of images doesnt equal to {amount}"
    assert pattern.match(imgs[utils.rnd_el(imgs)]), "Not appropriate link for the image"


@pytest.mark.parametrize(
    "breed",
    [utils.rnd_breed(utils.build_link(url_api, "/breeds/list/all")) for i in range(3)],
)
def test_breed_imgs(breed, build_link_breed):
    res = requests.get(f"{build_link_breed}/{breed}/images")
    imgs = res.json().get("message")
    assert res.status_code == 200, "Status code is not 200"
    assert res.json().get("status") == stat_ok, 'Status doesnt equal "success"'
    assert len(set(imgs)) == len(imgs), "List contains doubles"


@pytest.mark.parametrize("breed", utils.random_breeds(), ids=lambda b: f'breed={b}')
def test_all_subbreeds(breed, build_link_breed, build_link_all_breeds):
    res = requests.get(f"{build_link_breed}/{breed}/list")
    res_all = requests.get(build_link_all_breeds)
    all_breeds = res_all.json().get("message")
    subbreeds = res.json().get("message")
    assert res.status_code == 200, "Status code is not 200"
    assert res.json().get("status") == stat_ok, 'Status doesnt equal "success"'
    assert len(set(subbreeds)) == len(subbreeds), "List contains doubles"
    assert all_breeds[breed] == subbreeds
