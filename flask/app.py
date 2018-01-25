#from flask import Flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def my_form():
    #return 'Hello World!'
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()
    return processed_text

# Get js buttons where only 1 can be selected at a time for graph, list, and code

# Get request with params, which will get a graph of neo4j artists connected to this node
def get_artists_graph(params):
    # Do neo4j query

@get("/movie/<name>")
def get_movie(title):
    """ Page with details for a specific movie.
    """
    return render_template("movie", movie=Movie.select(graph, title).first())


if __name__ == '__main__':
    app.run()
