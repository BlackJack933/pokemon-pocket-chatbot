import sqlite3

def get_connection():
    return sqlite3.connect('pokemon_pocket.db')

def create_tables():
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS pokemon_cards (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
                        name TEXT NOT NULL,
                        set_name TEXT NOT NULL,
                        rarity TEXT NOT NULL,
                        trainer_type TEXT NOT NULL,
                        effect TEXT NOT NULL
                    );
                ''')

    conn.commit()
    conn.close()

def insert_pokemon_card(name, set_name, rarity, stage, hp, types, attacks, weaknesses, retreat, boosters, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO pokemon_cards (name, set_name, rarity, stage, hp, types, attacks, weaknesses, retreat, boosters, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, set_name, rarity, stage, hp, types, attacks, weaknesses, retreat, boosters, description))

    conn.commit()
    conn.close()

def insert_trainer_card(name, set_name, rarity, trainer_type, effect):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO trainer_cards (name, set_name, rarity, trainer_type, effect)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, set_name, rarity, trainer_type, effect))

    conn.commit()
    conn.close()

    