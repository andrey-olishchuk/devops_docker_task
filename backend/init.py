from main import db
from main import Message
db.create_all()

initmsg = Message(msg='test')
db.session.add(initmsg)
db.session.commit()