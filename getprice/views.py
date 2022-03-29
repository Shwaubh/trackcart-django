from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
from bs4 import BeautifulSoup
import re


@api_view(['GET'])
def price(request):
    data = {}
    data['price'] = []
    link = request.GET['link'].split(",")
    for link in link:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        soup = soup.find_all(string=re.compile("^(₹)"))[0]
        data['price'].append(soup)
    return Response(data)


