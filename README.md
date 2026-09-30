# 📒 Ledger

**One list. No clutter. Just what needs doing.**

Ledger is a minimal, dark-themed todo list app built with Flask. Unlike most todo apps that rely on a database, every task is stored as its own plain-text `.txt` file on disk, making the app's storage completely transparent and easy to inspect, back up, or edit by hand.

---

## ✨ Features

- ➕ **Add tasks** with a title and an optional short description
- ✅ **Mark tasks complete** — completed todos move to their own section, shown with a strikethrough
- 🗑️ **Delete tasks**, active or completed
- 📂 **File-based storage** — each todo is saved as a plain `.txt` file, no database required
- 🧼 **Filename sanitization** — todo titles are cleaned before being used as filenames, stripping unsafe characters
- 🎨 Sleek dark UI with a two-column layout (active vs. completed) and a monospace/sans-serif font pairing

---

## 🛠️ Tech Stack

- **Python 3** + **Flask** — routing and server-side logic
- **Jinja2** — server-side templating (`render_template`)
- **Plain `.txt` files** — used as the storage layer instead of a database
- **HTML5 / CSS3** — custom-styled frontend, no CSS framework
- **Google Fonts** — JetBrains Mono (headings) & Inter (body)

---

## 📁 Project Structure

```
ledger/
├── app.py                  # Flask application (routes + file-based storage logic)
├── todos/                  # Auto-created folder where each todo is saved as a .txt file
├── templates/
│   └── index.html          # Main page template (Jinja2)
├── static/
│   └── style.css           # Stylesheet
└── README.md
```

> **Note:** The `todos/` folder is created automatically the first time the app runs (`os.makedirs(TODOS_FOLDER, exist_ok=True)`), so it doesn't need to exist in the repo beforehand.

---

## 📄 How Todos Are Stored

Each todo is saved as `todos/<title>.txt`, with a simple two-line format:

```
pending
Optional description text goes here
```

The first line holds the status (`pending` or `complete`), and everything after it is the description. The filename itself (minus the `.txt` extension) is used as the todo's title.

---

## 🔀 Routes

| Route                  | Method | Description                                  |
|--------------------------|--------|-------------------------------------------------|
| `/`                     | GET    | Displays active and completed todos           |
| `/add`                  | POST   | Creates a new todo file from the submitted form |
| `/complete/<title>`     | POST   | Marks a todo as complete                       |
| `/delete/<title>`       | POST   | Deletes a todo file                            |

---

## ▶️ Getting Started

### Prerequisites
- Python 3
- Flask

```
pip install flask
```

### Running the App

```
git clone https://github.com/rhitamcoder/ledger.git
```
```
cd ledger
```
```
python app.py
```

The app will start in debug mode at `http://127.0.0.1:5000/`. Add your first todo to see the `todos/` folder populate automatically.

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
