from sqlalchemy import create_engine
from models import User, Key, UserKeyLink, Base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://cad_root:root_pass@localhost:5432/cad_keysafe')

session = sessionmaker()
session.configure(bind=engine)
sess = session()

Base.metadata.create_all(engine)

# Added test data
key1 = Key(room="123", rfid_s="111", status=True)
key2 = Key(room="111", rfid_s="444", status=True)
key3 = Key(room="222", rfid_s="888", status=True)
user1 = User(firstname="John", lastname="Johnson", rfid_c="222")
user2 = User(firstname="Harry", lastname="Potter", rfid_c="333")
user3 = User(firstname="John", lastname="Cena", rfid_c="555")
user4 = User(firstname="Piter", lastname="Piterson", rfid_c="666")

sess.add_all([key1, key2, key3, user1, user2, user3, user4])

sess.commit()
engine.dispose()

ukl1 = UserKeyLink.user_get_key(user2, key2)
ukl2 = UserKeyLink.user_get_key(user3, key3)

ukl3 = UserKeyLink.user_return_key(key2)
ukl3 = UserKeyLink.user_get_key(user2, key2)

print "READY TO WORK"
#Close the connection

