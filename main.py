import flask
from urllib.parse import urlparse
from ReaperEngine import *

app = flask.Flask(__name__)
engine = ReaperEngine()

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def index(path):
    if not path:
        return engine.get_random_posts()
    if path == "_export":
        return engine.export_internet()

    parsed_path = urlparse("http://" + path)
    if parsed_path.path.startswith('/r/'):
        parts = parsed_path.path.split('/')
        if len(parts) > 2:
           subreddit_name = parts[1]
           post_id = parts[2]
           if flask.request.method == 'POST':
                comment_text = flask.request.form.get("comment")
                engine.add_comment(subreddit_name, post_id, comment_text)
           return engine.get_post(subreddit_name, post_id)
        else:
            return engine.get_subreddit(parts[1])
    
    generated_page = engine.get_page(parsed_path.netloc, path=parsed_path.path)
    return generated_page

if __name__ == "__main__":
    app.run(debug=True)