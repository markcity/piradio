#netsh advfirewall firewall add rule name="Open Port 5000" dir=in action=allow protocol=TCP localport=5000
#source bin/activate
from flask import Flask, request, render_template_string

from flask import jsonify
app = Flask(__name__)

@app.route('/ip')
def ip():
    html="hi your ip address is<br>"
    html = html + request.remote_addr
    return html

@app.route('/greet/<name>')
def greet(name):
    # Extract additional data from query parameters if needed
    age = request.args.get('age', 'unknown')
    
    print(jsonify({'ip': request.remote_addr}))
    
    # Create a simple HTML template
    html_template = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Greeting Page</title>
      </head>
      <body>
        <h1>Hello, {{ name }}!</h1>
        <p>Your age is {{ age }}.</p>
      </body>
    </html>
    '''
    
    # Render the template with dynamic data
    return render_template_string(html_template, name=name, age=age)

@app.route('/register/<name>/<type>')
def register(name,type):
    import secrets

    def generate_secure_token(length=32):
        return secrets.token_hex(length)

    # Example usage
    unique_hash = generate_secure_token()


    import sqlite3
    # Connect to the database (or create it)
    conn = sqlite3.connect('useful.db')

    # Create a cursor object
    cursor = conn.cursor()
    cursor.execute('''
      INSERT INTO register (id, name, type) VALUES (?, ?, ?)
    ''', (unique_hash, name,type))

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()


    return unique_hash


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)