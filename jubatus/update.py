#!/usr/bin/env python
# -*- coding:utf-8 -*-

host = '127.0.0.1'
port = 9199
name = 'dmp'

import jubatus
from jubatus.common import Datum

import json

LEARNING_JSON_PATH = './ads/ads.json'


def connect_jubatus():
    client = jubatus.Recommender(host, port, name)
    return client


def update(learning_json_path):
    client = connect_jubatus()
    with open(learning_json_path) as f:
        learning_data = json.load(f)
    for key, value in learning_data.items():
        d = Datum(value)
        client.update_row(key,d)
        print key, value

def main():
    update(LEARNING_JSON_PATH)

if __name__ == '__main__':
    main()
