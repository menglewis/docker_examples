from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = psycopg2.connect(
        dbname='tutorial',
        user='dev',
        password='dev',
        host='db'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM test.names;")
    results = cursor.fetchall()

    return f'''Hello, World!
<br><br>
{"<br>".join(row[0] for row in results)}
    '''
