
import requests
from auth import get_acces_token

ENDPOINT = 'https://api.spotify.com'


def get_user_info()
	"""
	"""
	#example headers :  H = {'Authorization': 'Bearer BQC2XMtIjpWM2s6vck_NYaMS864hlH-EAwn791Biwp6qMl2aJvI-l4LaoJqeSVdxatEICCS-w_XqAPCkc_uuWoIqpTiN6TXOhsJiqO1OudYk49c8EIgRr9-noeUmcMHqo8s4lH-OjK6h622xe-rX7x2zBeCQaLwbUqu5kzLo'}
	headers = {'Authorization': 'Bearer : {}'.format(get_acces_token())}

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

	return response.json()

