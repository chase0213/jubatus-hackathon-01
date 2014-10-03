#!/usr/bin/env python
# -*- coding: utf-8 -*-

host = '127.0.0.1'
port = 9199
name = 'dmp'

import jubatus
from jubatus.common import Datum
from django.http import HttpResponse

import json


def connect_jubatus():
    client = jubatus.Recommender(host, port, name)
    return client


def analyze(obj):
    client = connect_jubatus()
    d = Datum(obj)
    sr = client.similar_row_from_datum(d, 100)
    return sr


def index(request):
    text = ""
    if request.method == 'GET':
        text = request.GET["text"]
    data = { "text": text }
    sr = analyze(data)
    json_obj = {}
    for r in sr:
        json_obj[r.id] = r.score
        print r.id, "with score", r.score
    return HttpResponse(json.dumps(json_obj), content_type="application/json")
