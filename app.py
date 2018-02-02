import boto3
from chalice import Chalice

from chalicelib.global_constants import EMOJI
from chalicelib.kudos_bot import handle_message

app = Chalice(app_name='kudosbot')
app.debug = True


@app.route('/')
def index():
    return f"THE {EMOJI} BOT IS ALIVE!!"


@app.route('/handle-message', methods=['POST'])
def create_user():
    request = app.current_request.json_body
    response = handle_message(request)
    return response or "200 OK"
