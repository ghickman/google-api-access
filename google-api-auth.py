import urllib
import webbrowser

import requests


def run():
    CLIENT_ID = raw_input('Client ID: ')
    CLIENT_SECRET = raw_input('Client Secret: ')
    SCOPE = raw_input('Scopes (space delimited): ')

    query = {
        'scope': SCOPE,
        'state': 'something',
        'redirect_uri': 'http://localhost:8000',
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'approval_prompt': 'force',
        'access_type': 'offline',
    }
    params = urllib.urlencode(query)
    url = 'https://accounts.google.com/o/oauth2/auth?{0}'.format(params)
    print('Opening authorization URL, please follow the instructions then copy/paste the "code" param here.')
    print(url)
    webbrowser.open_new_tab(url)

    code = raw_input('Code: ')

    payload = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': 'http://localhost:8000',
        'grant_type': 'authorization_code',
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = 'https://accounts.google.com/o/oauth2/token'
    r = requests.post(url, data=payload, headers=headers)
    r.raise_for_status()

    print('Access Token: {0}'.format(r.json()['access_token']))
    print('Refresh Token: {0}'.format(r.json()['refresh_token']))

if __name__ == '__main__':
    run()
