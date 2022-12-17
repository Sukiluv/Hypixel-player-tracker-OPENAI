import requests
import json

# Replace YOUR_API_KEY with your actual Hypixel API key
API_KEY = 'YOUR_API_KEY'

# Replace PLAYER_UUID with the UUID of the player you want to track
PLAYER_UUID = 'PLAYER_UUID'

# Make a GET request to the Hypixel API to retrieve player information
response = requests.get(f'https://api.hypixel.net/player?key={API_KEY}&uuid={PLAYER_UUID}')

# Check the status code of the response to make sure the request was successful
if response.status_code != 200:
    print('An error occurred while retrieving player information')
else:
    # Parse the response as JSON
    player_data = response.json()
    print(f'Player name: {player_data["player"]["displayname"]}')

# Make a GET request to the antisniper API to retrieve player activity information
response = requests.get(f'https://api.antisniper.com/player/{PLAYER_UUID}')

# Check the status code of the response to make sure the request was successful
if response.status_code != 200:
    print('An error occurred while retrieving player activity information')
else:
    # Parse the response as JSON
    activity_data = response.json()
    print(f'Player last seen: {activity_data["last_seen"]}')
