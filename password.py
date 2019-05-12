from api.hash import hash, verify

stored_password = hash('secret')
print(stored_password)
result = verify(stored_password, 'secrets')
print(result)