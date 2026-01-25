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
    breeds = [breed for breed in res.json().get("message")]
    return breeds[rnd_el(breeds)]


def rnd_el(arr):
    return random.randint(0, len(arr) - 1)


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
