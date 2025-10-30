from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    books = [
        {"title": "Dune", "synopsis": "A sci-fi epic about giant sandworms and space politics."},
        {"title": "The Hobbit", "synopsis": "A small person goes on a big adventure with wizards and dwarves."},
        {"title": "1984", "synopsis": "A very cheerful book about a perfect society where everyone is happy."},
    ]
    tags = ["Sci-Fi", "Fantasy", "Classic", "Dystopian", "Adventure"]
    
    return render_template('index.html', books=books, tags=tags)

if __name__ == '__main__':
    app.run(debug=True)