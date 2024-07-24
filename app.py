from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/")
def render_template_users():
    response = get_users()
    return render_template('users.html', users=response['users'])

def get_users():
    try:
        response = requests.get('https://randomuser.me/api/?results=6')
        if response.status_code != 200: 
            raise "status code invalid"
        return{"status_code": response.status_code, "message": "operation sucessful", "users":response.json()['results']}
    except:
        return {"status_code": 500, "message": "conection error", "users":[]}

if __name__ == '__main__':
    app.run()