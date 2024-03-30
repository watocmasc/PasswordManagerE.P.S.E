import crypto_cipher as cr

# encrypt the database eventually
key = cr.load_key()
cr.decrypt('data.json', key)
cr.encrypt('data.json', key)