#!flask/bin/python
import six
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
from models import app, db, Users, Tasks

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    user = Users.query.filter_by(username=username).first()
    if user is None or user.username != 'miguel':
        return None
    return user.password


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def make_public_task(task):
    new_task = {}
    new_task['id'] = url_for('get_task', task_id=task.id, _external=True)
    new_task['title'] = task.title
    new_task['description'] = task.description
    new_task['done'] = task.done
    return new_task


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks':
                    [make_public_task(task) for task in Tasks.query.all()]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = Tasks.query.get(task_id)
    if task is None:
        abort(404)
    return jsonify({'task': make_public_task(task)})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    title = request.json['title']
    desc = request.json.get('description', ""),
    task = Tasks(title, desc)
    db.session.add(task)
    db.session.commit()
    return jsonify({'task': make_public_task(task)}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = Tasks.query.get(task_id)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and \
            not isinstance(request.json['title'], six.string_types):
        abort(400)
    if 'description' in request.json and \
            not isinstance(request.json['description'], six.string_types):
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description',
                                        task.description)
    task.done = request.json.get('done', task.done)
    db.session.add(task)
    db.session.commit()
    return jsonify({'task': make_public_task(task)})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if task is None:
        abort(404)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=False)
