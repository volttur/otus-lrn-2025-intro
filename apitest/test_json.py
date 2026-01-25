import pytest
from dotenv import load_dotenv
import requests
import os
import json
import utils

load_dotenv()
with open(os.environ.get('INFOPATH'), 'r') as f:
    info = json.load(f)


def test_all_posts(build_link_all_posts):
    res = requests.get(build_link_all_posts)
    posts = res.json()
    assert res.status_code == 200, 'Status code doesn\'t  equal 200'
    assert len(posts) == len(set([post['id'] for post in posts])), 'There are doubles in the list of ids'


@pytest.mark.parametrize('id', [utils.rnd_post_id() for _ in range(3)])
def test_get_post(id, build_link_all_posts):
    res = requests.get(utils.build_link(build_link_all_posts, f'/{id}'))
    post = res.json()
    assert res.status_code == 200, 'Status code doesn\'t equal 200'
    assert 'list' not in str(type(post)), 'There are several posts with same id` in the result' 
    assert post['title'] is not None


@pytest.mark.parametrize('id', [-1, 0, utils.last_post_id])
def test_get_post_negative(id, build_link_all_posts):
    res = requests.get(utils.build_link(build_link_all_posts, f'/{id}'))
    post = res.json()
    assert res.status_code == 404, 'Status code doesn\'t equal 404'
    assert len(post) == 0, 'Result is not empty'


def test_create_post(build_link_all_posts):
    title = utils.gen_title()
    body = utils.gen_body()
    user_id = utils.gen_user_id()
    data = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    res = requests.post(build_link_all_posts, data=data)
    post = res.json()
    assert res.status_code == 201, 'Status code doesn\'t equal 200'
    assert post['title'] == title, 'Title is empty'
    assert post['body'] == body, 'Body is empty'
    assert post['userId'] == str(user_id), 'UserId is empty'
    assert post['id'] is not None, 'Id is empty'


@pytest.mark.parametrize('id', [utils.rnd_post_id() for _ in range(3)])
def test_delete_post(id, build_link_all_posts):
    res = requests.delete(utils.build_link(build_link_all_posts, f'/{id}'))
    post = res.json()
    assert res.status_code == 200, 'Status code doesn\'t equal 200'
    assert len(post) == 0, 'Post was not deleted'
