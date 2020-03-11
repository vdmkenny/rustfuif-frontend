# -*- coding: utf-8 -*-
import requests
import humanize
from datetime import datetime
import dateutil.parser

def get_games(host="http://127.0.0.1:8080"):
    r = requests.get(f'http://{host}/api/games')
    games = r.json()
    for game in games:
        game['start_time_nt'] = humanize.naturaltime(dateutil.parser.isoparse(game['start_time']).replace(tzinfo=None))
        game['close_time_nt'] = humanize.naturaltime(dateutil.parser.isoparse(game['close_time']).replace(tzinfo=None))
    print(games)
    return games

def get_login_cookie(username, password, host="http://127.0.0.1:8080"):
    credentials = {
            'username': username,
            'password': password          
            }
    r = requests.post(f'http://{host}/api/login', json = credentials)
    if 200 <= r.status_code <= 299:
        return r.cookies['actix-session']
    else: 
        return False

def get_login_details(username, password, host="http://127.0.0.1:8080"):
    credentials = {
            'username': username,
            'password': password          
            }
    r = requests.post(f'http://{host}/api/login', json = credentials)
    if 200 <= r.status_code <= 299:
        return r.json()
    else: 
        return False

def create_new_game(cookies, game, host="http://127.0.0.1:8080"):
    r = requests.post(f'http://{host}/api/games', json = game, cookies=cookies)
    return r

def convert_timestamp(dt):
    # Our format is "March 18, 2020 13:50"
    date = datetime.strptime(dt, "%B %d, %Y %H:%M").isoformat()
    return f'{date}Z'


