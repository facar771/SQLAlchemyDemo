# %% Veritabanına Bağlanmak 
import psycopg2

databaseName = "db"
userName = "postgres"
password = "12345"
hostIp = "127.0.0.1"
hostPort = "5432"

baglanti = psycopg2.connect(database = databaseName,
                            user = userName,
                            password = password,
                            host = hostIp,
                            port = hostPort)

# %% VERİLERİ EKLEMEK

baglanti.autocommit = True
cursor = baglanti.cursor()

items = [
        ("Aqua", "Red"),
        ("Vesel", "White"),
        ("200C", "Black"),
        ]

carRecord = ", ".join(["%s"] * len(items))

queryInsert = (
    f"INSERT INTO items (title, description) VALUES {carRecord}")

cursor.execute(queryInsert, items)

# %% VERİLERİ EKLEMEK2

baglanti.autocommit = True
cursor = baglanti.cursor()

users = [
        ("mail1", "1234", False),
        ("mail2", "12345", True),
        ("mail3", "123456", True),
        ]

carRecord = ", ".join(["%s"] * len(users))

queryInsert = (
    f"INSERT INTO users (email, hashed_password, is_active) VALUES {carRecord}")

cursor.execute(queryInsert, users)
