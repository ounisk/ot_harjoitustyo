from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulut ja kaiken sisällön.

    Args:
        connection (connection -olio): olio tietokantayhteyttä varten.
    """
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS GROCERIES 
        ''')

    cursor.execute('''
        DROP TABLE IF EXISTS HISTORY 
        ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.
    Args:
        connection (connection -olio): olio tietokantayhteyttä varten.
    """
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE GROCERIES (
            id INTEGER PRIMARY KEY,
            product TEXT,
            quantity INTEGER,
            store TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE HISTORY (
            id INTEGER PRIMARY KEY,
            product TEXT,
            store TEXT
        );
    ''')

    connection.commit()


def initialize_database():
    """Metodikutsu, joka aktivoi tietokantayhteyden mahdollistavan yhteyden.

    Lisäksi alustaa taulut: kutsuu tietokantataulujen poisto- ja luonti-metodit.

    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
