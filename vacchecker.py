import requests

# Replace with your own Steam API key
API_KEY = "YOUR_API_KEY"

# The SteamID64 of the user you want to fetch data for
steam_id64 = "76561199475413939"

# URL for retrieving the player's summary
url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={API_KEY}&steamids={steam_id64}"

# Fetch the player's data
response = requests.get(url)
data = response.json()

# Check if the response is valid
if 'response' in data and 'players' in data['response']:
    player = data['response']['players'][0]
    
    # Extract and display relevant information
    player_name = player.get('personaname', 'N/A')
    profile_url = player.get('profileurl', 'N/A')
    vac_banned = player.get('vac_banned', False)
    country = player.get('loccountrycode', 'N/A')
    location = player.get('location', 'N/A')
    profile_created = player.get('timecreated', 'N/A')

    print(f"Player Info for {player_name} (SteamID64: {steam_id64}):\n")
    print(f"Steam Profile URL: {profile_url}")
    print(f"VAC Banned: {'Yes' if vac_banned else 'No'}")
    print(f"Country: {country}")
    print(f"Location: {location}")
    print(f"Profile Created: {profile_created}")

    # Optionally, you can also retrieve owned games or achievements here
    # Example: Get owned games for this player
    games_url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={steam_id64}&include_appinfo=true"
    games_response = requests.get(games_url)
    games_data = games_response.json()

    if 'response' in games_data and 'games' in games_data['response']:
        print("\nOwned Games:")
        for game in games_data['response']['games']:
            print(f"- {game['name']} (AppID: {game['appid']})")
else:
    print("Error: Could not retrieve player data.")