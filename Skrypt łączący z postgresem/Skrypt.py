import psycopg2
try:
    #tworzymy strin (text) zawierającą bazy danych
    connectionString = "dbname='alamakota' user='xyz' host='127.0.0.1' password='12345'"
    #Połączenie z bazą
    connection = psycopg2.connect(connectionString)
    #Tworzymy wskaźnik
    cursor = connection.cursor()
    #Działanie na wskaźniku
    cursor.execute("""Select * FROM iso;""")
    #Wylistowanie rekordów z bazy
    for record in cursor:
        print(record[1])



except Exception as error:
    print('Błąd:')
    print(error)
