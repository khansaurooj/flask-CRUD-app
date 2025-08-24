from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

#  Database Handler Class
class MySQLHandler:
    def __init__(self, host="localhost", user="root", password="urooj#123", database="khansa"):
        self.db_config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def get_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]
        cursor.close()
        conn.close()
        return tables

    def add_record(self, table, name, age):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(f"INSERT INTO {table} (name, age) VALUES (%s, %s)", (name, age))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()

    def get_table_data(self, table):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()
        return rows, columns

    def delete_record(self, table, record_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(f"DELETE FROM {table} WHERE id = %s", (record_id,))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()

#  Create handler object
db = MySQLHandler()

#                             =======================
#                              Flask Routes (Use class)
#                             =======================

@app.route('/')
def home():
    tables = db.get_tables()
    return render_template("home.html", tables=tables)

@app.route('/add', methods=['GET', 'POST'])
def add():
    tables = db.get_tables()
    if request.method == 'POST':
        table = request.form['table']
        name = request.form['name']
        age = request.form['age']
        success = db.add_record(table, name, age)
        if success:
            return redirect('/')
        else:
            return "Error: Could not insert data. Table may not exist or record might be duplicate."
    return render_template("add.html", tables=tables)

@app.route('/view/<table>')
def view_table(table):
    rows, columns = db.get_table_data(table)
    return render_template("view.html", table=table, rows=rows, columns=columns)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    tables = db.get_tables()
    if request.method == 'POST':
        table = request.form['table']
        record_id = request.form['id']
        success = db.delete_record(table, record_id)
        if success:
            return redirect('/')
        else:
            return " Error deleting the record. Please check table and ID."
    return render_template("delete.html", tables=tables)

# ▶ Run App
if __name__ == '__main__':
    app.run(debug=True)
