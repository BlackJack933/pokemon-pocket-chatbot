import sqlite3

# this function establishes a connection to the SQLite database
def get_connection():
    return sqlite3.connect('pokemon_pocket.db')

# this function creates the necessary tables in the database if they do not already exist
def create_tables():
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS pokemon_cards (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        card_id TEXT NOT NULL UNIQUE,
                        name TEXT NOT NULL,
                        set_name TEXT NOT NULL,
                        rarity TEXT NOT NULL,
                        stage TEXT NOT NULL,
                        hp INTEGER NOT NULL,
                        types TEXT NOT NULL,
                        attacks TEXT NOT NULL,
                        weaknesses TEXT,
                        retreat INTEGER,
                        boosters TEXT NOT NULL,
                        description TEXT
                    );
                ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS trainer_cards (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        card_id TEXT NOT NULL UNIQUE,
                        name TEXT NOT NULL,
                        set_name TEXT NOT NULL,
                        rarity TEXT NOT NULL,
                        trainer_type TEXT NOT NULL,
                        effect TEXT NOT NULL
                    );
                ''')
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS decks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        slug TEXT NOT NULL UNIQUE,
                        meta_share FLOAT NOT NULL,
                        win_rate FLOAT NOT NULL,
                        cards TEXT NOT NULL
                    );
                ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS matchups (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        deck_id INT NOT NULL,
                        opponent_deck_id INT NOT NULL ,
                        wins INT NOT NULL,
                        losses INT NOT NULL,
                        ties INT NOT NULL,
                        win_rate FLOAT NOT NULL,
                        FOREIGN KEY (deck_id) REFERENCES decks(id),
                        FOREIGN KEY (opponent_deck_id) REFERENCES decks(id)
                    );
                ''')

    conn.commit()
    conn.close()

# this function inserts a Pokémon card into the database
def insert_pokemon_card(card_id, name, set_name, rarity, stage, hp, types, attacks, weaknesses, retreat, boosters, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO pokemon_cards (card_id, name, set_name, rarity, stage, hp, types, attacks, weaknesses, retreat, boosters, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (card_id, name, set_name, rarity, stage, hp, types, attacks, weaknesses, retreat, boosters, description))

    conn.commit()
    conn.close()

# this function inserts a Trainer card into the database
def insert_trainer_card(card_id, name, set_name, rarity, trainer_type, effect):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO trainer_cards (card_id, name, set_name, rarity, trainer_type, effect)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (card_id, name, set_name, rarity, trainer_type, effect))

    conn.commit()
    conn.close()

def insert_deck(name, slug, meta_share, win_rate, cards):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO decks (name, slug, meta_share, win_rate, cards)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, slug, meta_share, win_rate, cards))

    conn.commit()
    conn.close()

def insert_matchup(deck_id, opponent_deck_id, wins, losses, ties, win_rate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO matchups (deck_id, opponent_deck_id, wins, losses, ties, win_rate)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (deck_id, opponent_deck_id, wins, losses, ties, win_rate))

    conn.commit()
    conn.close()

    