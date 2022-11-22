import requests
import json
from types import SimpleNamespace
from bs4 import BeautifulSoup

def make_request(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')