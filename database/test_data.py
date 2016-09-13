from models import User, Key, UserKeyLink

users = [{"firstname": "Tony", "lastname": "Stark", "rfid_c": "11111"},
         {"firstname": "John", "lastname": "Smith", "rfid_c": "22222"},
         {"firstname": "Frank", "lastname": "Montana", "rfid_c": "33333"},
         {"firstname": "Gandalf", "lastname": "Gray", "rfid_c": "44444"},
         {"firstname": "Peter", "lastname": "Parker", "rfid_c": "55555"},
         {"firstname": "Mike", "lastname": "Sunny", "rfid_c": "66666"}]
keys = [{"room": "311", "rfid_s": "111"},
        {"room": "11D", "rfid_s": "444"},
        {"room": "212", "rfid_s": "222"},
        {"room": "555", "rfid_s": "555"},
        {"room": "343", "rfid_s": "333"}]

def create_users():
    for user in users:
        User.user_new(user['firstname'], user['lastname'], user['rfid_c'])

    for key in keys:
        Key.key_new(key['room'], key['rfid_s'])

    user1 = User.user_get_by_rfid(users[0]['rfid_c'])['data']
    user2 = User.user_get_by_rfid(users[1]['rfid_c'])['data']
    user3 = User.user_get_by_rfid(users[2]['rfid_c'])['data']
    user4 = User.user_get_by_rfid(users[3]['rfid_c'])['data']
    user5 = User.user_get_by_rfid(users[4]['rfid_c'])['data']
    user6 = User.user_get_by_rfid(users[5]['rfid_c'])['data']
    key1 = Key.key_get_by_rfid(keys[0]['rfid_s'])['data']
    key2 = Key.key_get_by_rfid(keys[1]['rfid_s'])['data']
    key3 = Key.key_get_by_rfid(keys[2]['rfid_s'])['data']
    key4 = Key.key_get_by_rfid(keys[3]['rfid_s'])['data']
    key5 = Key.key_get_by_rfid(keys[4]['rfid_s'])['data']

user1 = User.user_get_by_rfid(users[0]['rfid_c'])['data']
user2 = User.user_get_by_rfid(users[1]['rfid_c'])['data']
user3 = User.user_get_by_rfid(users[2]['rfid_c'])['data']
user4 = User.user_get_by_rfid(users[3]['rfid_c'])['data']
user5 = User.user_get_by_rfid(users[4]['rfid_c'])['data']
user6 = User.user_get_by_rfid(users[5]['rfid_c'])['data']
key1 = Key.key_get_by_rfid(keys[0]['rfid_s'])['data']
key2 = Key.key_get_by_rfid(keys[1]['rfid_s'])['data']
key3 = Key.key_get_by_rfid(keys[2]['rfid_s'])['data']
key4 = Key.key_get_by_rfid(keys[3]['rfid_s'])['data']
key5 = Key.key_get_by_rfid(keys[4]['rfid_s'])['data']

#import pdb;pdb.set_trace()
print "Start operations with keys"
UserKeyLink.userkeylink_return_key(key1.rfid_s)['data']
UserKeyLink.userkeylink_get_key(user1, key1.rfid_s)['data']

UserKeyLink.userkeylink_get_key(user2, key2.rfid_s)['data']
UserKeyLink.userkeylink_get_key(user3, key3.rfid_s)['data']
UserKeyLink.userkeylink_return_key(key2.rfid_s)['data']
