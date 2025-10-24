import psycopg2

try:
    conn = psycopg2.connect(
        host="demo-postgre-db.postgres.database.azure.com",
        database="myproject_db",
        user="Demo@demo-postgre-db",  # exact case
        password="CrudApp@2025",      # exactly as set in Azure
        port=5432,
        sslmode="require"
    )
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
