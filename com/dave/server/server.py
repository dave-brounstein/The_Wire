import com.dave.app.validation as application

from flask import Flask, jsonify, abort, request, make_response, url_for
from com.dave.app import process
from com.dave.error.exception import DataException, FieldException

app = Flask("theeye")

def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/theeye/event', methods=['POST'])
def create_events():
    try:
        application.validate_event(request.json)
    except FieldException as e:
        return make_response(jsonify({'error': e.message}), e.code)

    process.add(request.json)
    return make_response(jsonify({'message': 'Ok'}), 200)

@app.route('/theeye/event/session/<sessionId>', methods=['GET'])
def get_session(session_id):
    events = process.get_session(session_id)
    return make_response(jsonify(events), 200)

@app.route('/theeye/event/category/<catagory>', methods=['GET'])
def get_categories(category):
    try:
        application.validate_category(category)
        events = process.get_category(category)
        return make_response(jsonify(events), 200)

    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)

@app.route('/theeye/event', methods=['GET'])
def get_events():
    try:
        # todo: validate json
        start = request.json['start_time']
        end = request.json.get('end_time')
        duration = request.json.get('duration_seconds')
        if end:
            events = process.get_by_time(start, end)
        elif duration:
            events = process.get_by_duration(start, duration)
        else:
            return make_response(jsonify({'error': 'bad data'}), 400)

        return make_response(jsonify(events), 200)

    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
