from ellingtonia.app.jinjaconf import messenger
from flask import Flask
app = Flask(__name__)

@app.route('/gday')
def hello_world():
    return 'Hello World!'

@app.route('/')
def index():
	return 'index page here'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# if __name__ == '__main__':
app.run()