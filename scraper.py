import requests
import json
from database import create_tables, insert_pokemon_card, insert_trainer_card
import time

# this function fetches all the sets from the TCGDex API
def get_all_sets():
    url = "https://api.tcgdex.net/v2/en/series/tcgp"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['sets']
    else:
        print(f"Failed to fetch sets: {response.status_code}")
        return []

# this function fetches all the cards for a specific set from the TCGDex API
def get_cards_for_set(set_id):
    url = f"https://api.tcgdex.net/v2/en/sets/{set_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['cards']
    else:
        print(f"Failed to fetch cards for set {set_id}: {response.status_code}")
        return []

# this function fetches a specific card by its ID from the TCGDex API
def get_card_by_id(card_id):
    url = f"https://api.tcgdex.net/v2/en/cards/{card_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch card {card_id}: {response.status_code}")
        return []

# this function scrapes all cards from the TCGDex API
def scrape_all_cards():
    create_tables()
    for n in get_all_sets():
        time.sleep(0.5)
        for set in get_cards_for_set(n['id']):
            time.sleep(0.5)
            card = get_card_by_id(set['id'])
            
            if card['category'] == "Pokemon":
                attacks = json.dumps(card.get('attacks', []))
                weaknesses = json.dumps(card.get('weaknesses', []))
                retreat = card.get('retreat')
                boosters = json.dumps(card.get('boosters', []))
                types = json.dumps(card.get('types', []))
                insert_pokemon_card(card['name'], card['set']['name'], card['rarity'], card['stage'], card['hp'], types, attacks, weaknesses, retreat, boosters, card.get('description'))
            else:
                insert_trainer_card(card['name'], card['set']['name'], card['rarity'], card['trainerType'], card['effect'])
                

if __name__ == "__main__":
    scrape_all_cards()