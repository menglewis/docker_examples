from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname='tutorial', 
    user='dlewis',
    password='dlewis',
    host='db'
)
cursor = conn.cursor()

@app.route('/')
def hello_world():
    cursor.execute("SELECT name FROM test.names;")
    results = cursor.fetchall()

    return f'''Hello, World!
<br><br>
{"<br>".join(row[0] for row in results)}
    '''
