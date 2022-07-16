import os

from marshmallow.exceptions import ValidationError
from flask import Flask, request, abort

from project_data import utils
from project_data.commands import CommandsSchema, Commands
from project_data.config import DATA_DIR

app = Flask(__name__)


@app.route('/perform_query/', methods=['GET', 'POST'])
def perform_query():
    try:
        commands: Commands = CommandsSchema().load(request.args)
        file_path: str = os.path.join(DATA_DIR, commands.file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError('Wrong filename given')

        with open(file_path, 'r') as file:
            cmd1_result = getattr(utils, commands.cmd1)(file, commands.value1)
            cmd2_result = getattr(utils, commands.cmd2)(cmd1_result, commands.value2)
            return app.response_class('\n'.join([line.strip() for line in cmd2_result]), content_type="text/plain")

    except (ValueError, FileNotFoundError, TypeError, IndexError, ValidationError) as e:
        abort(400, e)


if __name__ == '__main__':
    app.run()