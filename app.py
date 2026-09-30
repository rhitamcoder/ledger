from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
TODOS_FOLDER = "todos"

# the todos folder exists when the app starts
os.makedirs(TODOS_FOLDER, exist_ok=True)

def sanitize_filename(title):
    #remove characters that aren't safe to use in a filename
    safe_chars = [c for c in title if c.isalnum() or c in (" ", "-", "_")]
    return "".join(safe_chars).strip()

def read_todo(filename):
    file_path = os.path.join(TODOS_FOLDER, filename)
    with open(file_path, "r") as f:
        lines = f.readlines()

    status = lines[0].strip()
    description = "".join(lines[1:]).strip()
    title = filename[:-4] # remove the ".txt" extension

    return {"title": title, "description": description, "status": status}


@app.route("/")
def home():
    filenames = os.listdir(TODOS_FOLDER)

    active_todos = []
    completed_todos = []

    for filename in filenames:
        todo = read_todo(filename)
        if todo["status"] == "complete":
            completed_todos.append(todo)
        else:
            active_todos.append(todo)

    return render_template("index.html", active_todos=active_todos, completed_todos=completed_todos)

@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title")
    description = request.form.get("description", "")

    safe_title = sanitize_filename(title)
    file_path = os.path.join(TODOS_FOLDER, f"{safe_title}.txt")

    with open(file_path, "w") as f:
        f.write("pending\n")
        f.write(description)

    return redirect(url_for("home"))

@app.route("/complete/<title>", methods=["POST"])
def complete_todo(title):
    file_path = os.path.join(TODOS_FOLDER, f"{title}.txt")

    with open(file_path, "r") as f:
        lines = f.readlines()

    description = "".join(lines[1:])

    with open(file_path, "w") as f:
        f.write("complete\n")
        f.write(description)

    return redirect(url_for("home"))

@app.route("/delete/<title>", methods=["POST"])
def delete_todo(title):
    file_path = os.path.join(TODOS_FOLDER, f"{title}.txt")

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

