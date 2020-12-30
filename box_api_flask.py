from boxsdk import OAuth2, Client
from flask import Flask, redirect, request
from box_api import get_child_items, get_folder_information


app = Flask(__name__)


oauth = OAuth2(
    client_id='',
    client_secret=''
)
# auth = OAuth2(
#     client_id='',
#     client_secret='',
#     access_token='',
# )
# client = Client(auth)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login')
def login():
    redirect_url = 'http://localhost:5000/login-success'
    auth_url, csrf_token = oauth.get_authorization_url(redirect_url)
    return redirect(auth_url, code=302)


@app.route('/login-success')
def login_success():
    code: str = request.args.get('code')
    access_token, refresh_token = oauth.authenticate(code)
    client = Client(oauth)

    root_folder_id = '123456789'
    root_folder = get_folder_information(client, root_folder_id)
    folders = get_child_items(client, root_folder)

    return f'<dir><a href="/login">Back to login</a></dir>'\
        f'<div>{folders.to_json()}</div>'


if __name__ == "__main__":
    app.run(debug=True)
