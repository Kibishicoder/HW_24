import os

from flask import Flask, request, abort

import utils
from config import DATA_DIR, COMMANDS

app = Flask(__name__)


@app.route('/perform_query/', methods=['GET', 'POST'])
def perform_query():

    file_name = request.json.get('file_name')
    cmd1 = request.json.get('cmd1') + '_'
    value1 = request.json.get('value1')
    cmd2 = request.json.get('cmd2') + '_'
    value2 = request.json.get('value2')

    # Check upcoming data
    if (
        None in (file_name, cmd1, value1, cmd2, value2)
        or cmd1 not in COMMANDS
        or cmd2 not in COMMANDS
    ):
        return abort(400, 'Wrong params given')

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, 'Wrong filename given')

    try:
        with open(file_path, 'r') as file:
            result_1 = getattr(utils, cmd1)(file, value1)
            result_2 = getattr(utils, cmd2)(result_1, value2)
    except (ValueError, TypeError) as e:
        abort(400, e)

    return app.response_class(result_2, content_type="text/plain")


if __name__ == '__main__':
    app.run()