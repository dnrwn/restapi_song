import json

from cryptography.fernet import Fernet

def decrypt(key, value):
    data = Fernet(key)
    if isinstance(value, bytes):
        data_d = data.decrypt(value)
        data_de = data_d.decode('utf-8')
        print(1)
    else:
        data_de = data.decrypt(value.encode('utf-8'))
        print(2)
    return json.loads(data_de.decode('utf-8'))


def key_read():
    with open('db_f/key', 'rb') as file:
        return file.read()

def value_read():
    with open('db_f/value', 'r', encoding='utf-8') as file:
        return file.read()


d = decrypt(key=key_read(), value=value_read())

# print(key_read())
# print(value_read())
