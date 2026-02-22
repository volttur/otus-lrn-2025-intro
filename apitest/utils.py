import random
from faker import Faker
from faker.providers import BaseProvider
from dotenv import load_dotenv
import os
import requests
import json

faker = Faker()

load_dotenv()
with open(os.environ.get("INFOPATH")) as f:
    info = json.load(f)
url = info["urls"]["url_api_brew"]
url_json = info["urls"]["url_api_json"]
url_api = info["urls"]["url_api"]


class RndNum(BaseProvider):
    def rnd_post_id(self):
        res = requests.get(build_link(url_json, "/posts"))
        ids = [post["id"] for post in res.json()]
        return ids[random.randint(0, len(ids) - 1)]


faker.add_provider(RndNum)


def build_link(base, endp):
    return f"{base}{endp}"


def rnd_breed(link):
    res = requests.get(link)
    assert res.status_code == 200, 'Cant get random breed'
    assert res.json().get("status") == "success", 'Cant get random breed'
    breeds = [breed for breed in res.json().get("message")]
    return breeds[rnd_el(breeds)]


def rnd_el(arr):
    rnd_num = None
    if arr == []:
        raise Exception()
    try:
        rnd_num = random.randint(0, len(arr) - 1)
    except Exception:
        print('Array for rnd_el func is empty')
    else:
        return rnd_num


def rnd_city():
    res = requests.get(build_link(url, "/breweries"))
    cities = list(map(lambda x: x["city"], res.json()))
    return cities[rnd_el(cities)]


def rnd_id():
    res = requests.get(build_link(url, "/breweries"))
    cities = list(map(lambda x: x["id"], res.json()))
    return cities[rnd_el(cities)]


def rnd_uuid():
    return faker.uuid4()


def rnd_post_id():
    return faker.rnd_post_id()


def last_post_id():
    res = requests.get(url)
    posts = res.json()
    if posts is not None and "list" in str(type(posts)):
        return len(posts)


def gen_title():
    return faker.sentence(random.randint(3, 6))


def gen_body():
    return faker.text(200)


def gen_user_id():
    return random.randint(1, 9)


def random_breeds(n=3):
    url_all = build_link(url_api, '/breeds/list/all')
    return [rnd_breed(url_all) for _ in range(n)]
