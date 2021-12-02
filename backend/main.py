from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
CORS(app)

@app.route('/')
def is_alive():
    return jsonify('live')


@app.route('/api/msg/<string:msgtext>', methods=['POST'])
def msg_post_api(msgtext):
    print(f"msg_post_api with message: {msgtext}")
    # TODO: store msg in DB and return identifier
    message = Message(msg=msgtext)
    db.session.add(message)
    db.session.commit()
    db.refresh(message)
    return jsonify({'msg_id': message.id})


@app.route('/api/msg/<int:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    print(f"msg_get_api > msg_id = {msg_id}")
    # TODO: get msg from DB and return it
    message = Message.query.filter_by(id=msg_id).first()
    if message:
        mvalue = message.msg
    else:
        mvalue = None

    return jsonify({'msg': mvalue})


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.msg