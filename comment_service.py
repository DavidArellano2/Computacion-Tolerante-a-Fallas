from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(250), nullable=False)

db.create_all()

@app.route('/comments/<int:book_id>', methods=['GET'])
def get_comments(book_id):
    book_comments = Comment.query.filter_by(book_id=book_id).all()
    comment_list = [{'id': comment.id, 'comment': comment.comment} for comment in book_comments]
    return jsonify({'comments': comment_list})

if __name__ == '__main__':
    app.run(port=5002)
