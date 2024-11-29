from flask import Flask, request, render_template, url_for, redirect
import requests

app = Flask(__name__)

BACKEND_API_URL = "http://127.0.0.1:8000"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        #route url
        SIGNUP_API = BACKEND_API_URL+'/signup'
        # collect data from the html templates and store it as a dictionary
        form_data = {
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        #requests.post
        response = requests.post(SIGNUP_API, form_data)
        if response.status_code == 200:
            return redirect(url_for('login'))
        return('Error')
    return render_template('signup.html')
        

@app.route('/user', methods=['GET', "POST"])
@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        #route url
        LOGIN_API = BACKEND_API_URL+'/login'
        # collect data from the html templates and store it as a dictionary
        form_data = {
            "username": request.form.get('username'),
            "password": request.form.get('password')
        }
        # requests.get
        response = requests.post(LOGIN_API, form_data)
        if response.status_code == 200:
            response_py = response.json()
            user = response_py.get('user', [])
            print(user)
            return render_template('dashboard.html', user=user)
        return('Error')
    return render_template('login.html')

@app.route('/all_users', methods=['GET', 'POST'])
def all_users():
    # url
    DASHBOARD_API = BACKEND_API_URL+'/all_users'
    response = requests.get(DASHBOARD_API)

    if response.status_code == 200:
        response_py = response.json()
        users = response_py.get('message', [])
        return render_template('all_users.html', users=users)
    else:
        return ('Error')


if __name__ == "__main__":
    app.run(port=5000, debug=True)