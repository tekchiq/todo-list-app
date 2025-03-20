# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database to store todo items
todos = []

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>Todo List</title>
    </head>
    <body>
        <h1>Todo List</title>
        <form method='POST' action='/add'>
            <input type='text' name='task' placeholder='Enter task' required>
            <button type='submit'>Add</button>
        </form>
        <ul>
            {todos}
        </ul>
    </body>
    </html>
    """.format(todos=''.join(f'<li>{todo}</li>' for todo in todos))

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        todos.append(task)
    return "", 303, {'Location': '/'}

if __name__ == '__main__':
    app.run(debug=True)
