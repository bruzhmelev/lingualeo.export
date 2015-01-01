#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import json
import http.cookiejar
import http.cookies
from http.cookiejar import CookieJar


class Lingualeo:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cj = CookieJar()

    def auth(self):
        url = "http://api.lingualeo.com/api/login"
        values = {
            "email": self.email,
            "password": self.password
        }
        return self.get_content(url, values)

    def add_word(self, word, tword):
        url = "http://api.lingualeo.com/addword"
        values = {
            "word": word,
            "tword": tword
        }
        return self.get_content(url, values)


    def get_translates(self, word):
        url_get_translate = "http://api.lingualeo.com/gettranslates?word=" + urllib.parse.quote_plus(word)

        try:
            result = self.get_content(url_get_translate, {})
            first_translate = result["translate"][0]
            return {
                "is_exist": result["is_user"],
                "word": word,
                "tword": first_translate["value"]
            }
        except Exception as e:
            return e.message

    def get_content(self, url, values):
        data = urllib.parse.urlencode(values)
        binary_data = data.encode('utf-8')

        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        req = opener.open(url, binary_data)

        return json.loads(req.read().decode('utf-8'))
