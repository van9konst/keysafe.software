from models import User, Key, UserKeyLink

users = [{"firstname": "Tony", "lastname": "Stark", "rfid_card": "11111", "admin": True,},
         {"firstname": "John", "lastname": "Smith", "rfid_card": "22222", "admin": False,},
         {"firstname": "Frank", "lastname": "Montana", "rfid_card": "33333", "admin": False,},
         {"firstname": "Gandalf", "lastname": "Gray", "rfid_card": "44444", "admin": True,},
         {"firstname": "Peter", "lastname": "Parker", "rfid_card": "55555", "admin": False,},
         {"firstname": "Mike", "lastname": "Sunny", "rfid_card": "66666", "admin": False,}]
keys = [{"room": "311", "rfid_chip": "111"},
        {"room": "11D", "rfid_chip": "444"},
        {"room": "212", "rfid_chip": "222"},
        {"room": "555", "rfid_chip": "555"},
        {"room": "343", "rfid_chip": "333"}]

def create_users():
    for user in users:
        import pdb;pdb.set_trace()
        User.create(user['firstname'], user['lastname'], user['rfid_card'], user['admin'])

    for key in keys:
        Key.create(key['room'], key['rfid_chip'])

create_users()

user1 = User.get_by_rfid(users[0]['rfid_card'])['data']
user2 = User.get_by_rfid(users[1]['rfid_card'])['data']
user3 = User.get_by_rfid(users[2]['rfid_card'])['data']
user4 = User.get_by_rfid(users[3]['rfid_card'])['data']
user5 = User.get_by_rfid(users[4]['rfid_card'])['data']
user6 = User.get_by_rfid(users[5]['rfid_card'])['data']
key1 = Key.get_by_rfid(keys[0]['rfid_chip'])['data']
key2 = Key.get_by_rfid(keys[1]['rfid_chip'])['data']
key3 = Key.get_by_rfid(keys[2]['rfid_chip'])['data']
key4 = Key.get_by_rfid(keys[3]['rfid_chip'])['data']
key5 = Key.get_by_rfid(keys[4]['rfid_chip'])['data']

#import pdb;pdb.set_trace()
print "Start operations with keys"
UserKeyLink.returning_key(key1.rfid_chip)['data']
UserKeyLink.getting_key(user1, key1.rfid_chip)['data']

UserKeyLink.getting_key(user2, key2.rfid_chip)['data']
UserKeyLink.getting_key(user3, key3.rfid_chip)['data']
UserKeyLink.returning_key(key2.rfid_chip)['data']
print "Done"
