from database import db_session
from models import User

new_user = User('Obama', 'Obama@localhost', '12344')
db_session.add(new_user)
db_session.commit()
