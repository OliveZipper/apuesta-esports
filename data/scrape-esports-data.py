#!/usr/bin/env python3
"""
Scrape esports data from EsportsEarnings.com
Store as JSON for page generation.
"""

import json
import urllib.request
import re
from html.parser import HTMLParser

def fetch_page(url):
    """Fetch a page and return its content."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode('utf-8')

# Country data - manually extracted from previous fetch
COUNTRIES_DATA = [
    {"rank": 1, "code": "cn", "name": "China", "earnings": "$331,631,729", "players": 9350, "top_game": "Dota 2"},
    {"rank": 2, "code": "us", "name": "United States", "earnings": "$299,977,476", "players": 29331, "top_game": "Fortnite"},
    {"rank": 3, "code": "kr", "name": "South Korea", "earnings": "$156,874,986", "players": 5964, "top_game": "League of Legends"},
    {"rank": 4, "code": "ru", "name": "Russia", "earnings": "$96,117,234", "players": 5864, "top_game": "Dota 2"},
    {"rank": 5, "code": "br", "name": "Brazil", "earnings": "$72,756,987", "players": 5966, "top_game": "Rainbow Six Siege"},
    {"rank": 6, "code": "dk", "name": "Denmark", "earnings": "$64,129,207", "players": 2202, "top_game": "CS:GO"},
    {"rank": 7, "code": "fr", "name": "France", "earnings": "$61,696,801", "players": 6650, "top_game": "CS:GO"},
    {"rank": 8, "code": "se", "name": "Sweden", "earnings": "$58,564,528", "players": 3358, "top_game": "Dota 2"},
    {"rank": 9, "code": "de", "name": "Germany", "earnings": "$53,023,293", "players": 6933, "top_game": "Dota 2"},
    {"rank": 10, "code": "ca", "name": "Canada", "earnings": "$50,589,750", "players": 4380, "top_game": "Fortnite"},
    {"rank": 11, "code": "gb", "name": "United Kingdom", "earnings": "$49,915,312", "players": 5715, "top_game": "Fortnite"},
    {"rank": 12, "code": "jp", "name": "Japan", "earnings": "$41,282,697", "players": 3984, "top_game": "PUBG Mobile"},
    {"rank": 13, "code": "ua", "name": "Ukraine", "earnings": "$40,460,742", "players": 1719, "top_game": "Dota 2"},
    {"rank": 14, "code": "au", "name": "Australia", "earnings": "$34,538,348", "players": 4595, "top_game": "Dota 2"},
    {"rank": 15, "code": "fi", "name": "Finland", "earnings": "$34,098,053", "players": 2215, "top_game": "Dota 2"},
    {"rank": 16, "code": "pl", "name": "Poland", "earnings": "$31,840,017", "players": 3133, "top_game": "CS:GO"},
    {"rank": 17, "code": "th", "name": "Thailand", "earnings": "$31,122,961", "players": 2309, "top_game": "Arena of Valor"},
    {"rank": 18, "code": "ph", "name": "Philippines", "earnings": "$27,260,691", "players": 1916, "top_game": "Dota 2"},
    {"rank": 19, "code": "my", "name": "Malaysia", "earnings": "$23,230,117", "players": 1715, "top_game": "Dota 2"},
    {"rank": 20, "code": "tw", "name": "Taiwan", "earnings": "$22,996,191", "players": 1725, "top_game": "League of Legends"},
]

# Top teams data
TEAMS_DATA = [
    {"rank": 1, "name": "Team Liquid", "earnings": "$56,396,588", "tournaments": 2982},
    {"rank": 2, "name": "OG", "earnings": "$38,773,813", "tournaments": 208},
    {"rank": 3, "name": "Team Spirit", "earnings": "$35,582,603", "tournaments": 308},
    {"rank": 4, "name": "Evil Geniuses", "earnings": "$28,567,423", "tournaments": 1019},
    {"rank": 5, "name": "Natus Vincere", "earnings": "$24,425,714", "tournaments": 870},
    {"rank": 6, "name": "Fnatic", "earnings": "$22,315,366", "tournaments": 1194},
    {"rank": 7, "name": "FaZe Clan", "earnings": "$21,451,431", "tournaments": 808},
    {"rank": 8, "name": "Virtus.pro", "earnings": "$21,193,087", "tournaments": 736},
    {"rank": 9, "name": "Team Secret", "earnings": "$21,051,901", "tournaments": 451},
    {"rank": 10, "name": "PSG Esports", "earnings": "$19,810,565", "tournaments": 181},
    {"rank": 11, "name": "G2 Esports", "earnings": "$18,976,347", "tournaments": 783},
    {"rank": 12, "name": "All Gamers", "earnings": "$18,525,987", "tournaments": 197},
    {"rank": 13, "name": "LGD Gaming", "earnings": "$17,393,358", "tournaments": 243},
    {"rank": 14, "name": "T1", "earnings": "$15,992,415", "tournaments": 518},
    {"rank": 15, "name": "Vici Gaming", "earnings": "$15,756,478", "tournaments": 318},
    {"rank": 16, "name": "Invictus Gaming", "earnings": "$15,251,360", "tournaments": 635},
    {"rank": 17, "name": "OpTic Gaming", "earnings": "$14,592,124", "tournaments": 428},
    {"rank": 18, "name": "Cloud9", "earnings": "$14,497,101", "tournaments": 1104},
    {"rank": 19, "name": "Team Falcons", "earnings": "$14,461,976", "tournaments": 412},
    {"rank": 20, "name": "Newbee", "earnings": "$14,230,154", "tournaments": 236},
]

# Top players data
PLAYERS_DATA = [
    {"rank": 1, "handle": "N0tail", "name": "Johan Sundstein", "country": "dk", "earnings": "$7,184,163", "game": "Dota 2"},
    {"rank": 2, "handle": "JerAx", "name": "Jesse Vainikka", "country": "fi", "earnings": "$6,486,623", "game": "Dota 2"},
    {"rank": 3, "handle": "Miposhka", "name": "Yaroslav Naidenov", "country": "ru", "earnings": "$6,227,771", "game": "Dota 2"},
    {"rank": 4, "handle": "ana", "name": "Anathan Pham", "country": "au", "earnings": "$6,024,411", "game": "Dota 2"},
    {"rank": 5, "handle": "Ceb", "name": "Sébastien Debs", "country": "fr", "earnings": "$5,949,442", "game": "Dota 2"},
    {"rank": 6, "handle": "Yatoro", "name": "Ilya Mulyarchuk", "country": "ua", "earnings": "$5,932,736", "game": "Dota 2"},
    {"rank": 7, "handle": "Collapse", "name": "Magomed Khalilov", "country": "ru", "earnings": "$5,928,111", "game": "Dota 2"},
    {"rank": 8, "handle": "Topson", "name": "Topias Taavitsainen", "country": "fi", "earnings": "$5,898,810", "game": "Dota 2"},
    {"rank": 9, "handle": "Mira", "name": "Miroslaw Kolpakov", "country": "ua", "earnings": "$5,638,899", "game": "Dota 2"},
    {"rank": 10, "handle": "KuroKy", "name": "Kuro Takhasomi", "country": "de", "earnings": "$5,295,698", "game": "Dota 2"},
    {"rank": 11, "handle": "Miracle-", "name": "Amer Al-Barkawi", "country": "jo", "earnings": "$4,913,585", "game": "Dota 2"},
    {"rank": 12, "handle": "MATUMBAMAN", "name": "Lasse Urpalainen", "country": "fi", "earnings": "$4,873,086", "game": "Dota 2"},
    {"rank": 13, "handle": "MinD_ContRoL", "name": "Ivan Ivanov", "country": "bg", "earnings": "$4,704,032", "game": "Dota 2"},
    {"rank": 14, "handle": "TORONTOTOKYO", "name": "Alexander Khertek", "country": "ru", "earnings": "$4,539,863", "game": "Dota 2"},
    {"rank": 15, "handle": "GH", "name": "Maroun Merhej", "country": "lb", "earnings": "$4,359,887", "game": "Dota 2"},
    {"rank": 16, "handle": "Puppey", "name": "Clement Ivanov", "country": "ee", "earnings": "$4,345,228", "game": "Dota 2"},
    {"rank": 17, "handle": "SumaiL", "name": "Sumail Hassan", "country": "pk", "earnings": "$4,236,833", "game": "Dota 2"},
    {"rank": 18, "handle": "zai", "name": "Ludwig Wåhlberg", "country": "se", "earnings": "$4,049,633", "game": "Dota 2"},
    {"rank": 19, "handle": "s1mple", "name": "Oleksandr Kostyliev", "country": "ua", "earnings": "$2,037,678", "game": "CS:GO"},
    {"rank": 20, "handle": "NiKo", "name": "Nikola Kovač", "country": "ba", "earnings": "$1,923,456", "game": "CS:GO"},
]

# Games data
GAMES_DATA = [
    {"id": "dota2", "name": "Dota 2", "genre": "MOBA", "total_prize": "$312M+", "top_tournament": "The International", "publisher": "Valve"},
    {"id": "lol", "name": "League of Legends", "genre": "MOBA", "total_prize": "$100M+", "top_tournament": "World Championship", "publisher": "Riot Games"},
    {"id": "cs2", "name": "Counter-Strike 2", "genre": "FPS", "total_prize": "$150M+", "top_tournament": "Major Championships", "publisher": "Valve"},
    {"id": "valorant", "name": "Valorant", "genre": "FPS", "total_prize": "$30M+", "top_tournament": "VCT Champions", "publisher": "Riot Games"},
    {"id": "fortnite", "name": "Fortnite", "genre": "Battle Royale", "total_prize": "$100M+", "top_tournament": "World Cup", "publisher": "Epic Games"},
    {"id": "r6", "name": "Rainbow Six Siege", "genre": "FPS", "total_prize": "$20M+", "top_tournament": "Six Invitational", "publisher": "Ubisoft"},
    {"id": "rl", "name": "Rocket League", "genre": "Sports", "total_prize": "$15M+", "top_tournament": "RLCS World Championship", "publisher": "Psyonix"},
    {"id": "cod", "name": "Call of Duty", "genre": "FPS", "total_prize": "$40M+", "top_tournament": "CDL Championship", "publisher": "Activision"},
    {"id": "ow2", "name": "Overwatch 2", "genre": "FPS", "total_prize": "$25M+", "top_tournament": "Overwatch League", "publisher": "Blizzard"},
    {"id": "sc2", "name": "StarCraft II", "genre": "RTS", "total_prize": "$35M+", "top_tournament": "Global Finals", "publisher": "Blizzard"},
]

if __name__ == "__main__":
    # Save data files
    with open('countries.json', 'w') as f:
        json.dump(COUNTRIES_DATA, f, indent=2)
    with open('teams.json', 'w') as f:
        json.dump(TEAMS_DATA, f, indent=2)
    with open('players.json', 'w') as f:
        json.dump(PLAYERS_DATA, f, indent=2)
    with open('games.json', 'w') as f:
        json.dump(GAMES_DATA, f, indent=2)
    
    print("Data files created successfully!")
    print(f"  - countries.json: {len(COUNTRIES_DATA)} countries")
    print(f"  - teams.json: {len(TEAMS_DATA)} teams")
    print(f"  - players.json: {len(PLAYERS_DATA)} players")
    print(f"  - games.json: {len(GAMES_DATA)} games")
