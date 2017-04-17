
import requests
from auth import get_acces_token

ENDPOINT = 'https://api.spotify.com'


def get_user_info()
	"""
	"""
	#example headers :  H = {'Authorization': 'Bearer BQC2XM...5kzLo'}
	headers = {'Authorization': 'Bearer : {}'.format(get_acces_token())}
	USER_URL = '{}/v1/me'.format(ENDPOINT)
	
	response = requests.get(USER_URL, headers=headers)

	# response example
	"""
	{u'birthdate': u'1986-08-08',
	 u'country': u'FR',
	 u'display_name': None,
	 u'email': u'oussaidslimane@gmail.com',
	 u'external_urls': {u'spotify': u'https://open.spotify.com/user/oussaidslimane'},
	 u'followers': {u'href': None, u'total': 0},
	 u'href': u'https://api.spotify.com/v1/users/oussaidslimane',
	 u'id': u'oussaidslimane',
	 u'images': [],
	 u'product': u'open',
	 u'type': u'user',
	 u'uri': u'spotify:user:oussaidslimane'}
	"""
	if response.status_code == 200:
		return True, response.json()
	return False, None

