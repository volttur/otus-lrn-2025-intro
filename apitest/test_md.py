import requests


def test_md(get_url, get_status_code):
    res = requests.get(get_url)
    assert str(res.status_code) == get_status_code
