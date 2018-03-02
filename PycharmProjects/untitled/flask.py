from flask import Flask, jsonify
from flask import abort
from flask import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t:t['id'] == task_id, tasks)
    if len(task) ==0:
        abort(404)

    return jsonify({'tasks': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
#curl -i http://localhost:5001/todo/api/v1.0/tasks
#curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5001/todo/api/v1.0/tasks
#curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5051/todo/api/v1.0/tasks/2
#curl -i -H 'Content-Type: application/json' -X PUT -d '{"done":true}' http://localhost:5001/todo/api/v1.0/tasks/2
#外层必须单影 内层必须双赢
#改进 1 return url for users not id
#2 put more security as httpauth
#3 system can serve more users , need user resources as to update get delete post for users
#4 make get method more detail set more parameter, do paging and fitering the data make it more valualbe
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051, debug=False)

