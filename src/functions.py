# -*- coding: utf-8 -*-
import requests

def get_games(host="http://127.0.0.1:8080"):
    r = requests.get(f'http://{host}/api/games')
    return r.json()

def get_login_cookie(username, password, host="http://127.0.0.1:8080"):
    credentials = {
            'username': username,
            'password': password          
            }
    r = requests.post(f'http://{host}/api/login', json = credentials)
    if r.status_code == 200:
        return r.cookies['actix-session']
    else: 
        return False
