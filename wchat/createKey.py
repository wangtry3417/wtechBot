from cryptography.fernet import Fernet

key = "DUBWKuYEugUex8ynVKm-7ctcUmwaV0u0JpzLkoka8_Q="

def create_key():
  fernet = Fernet(key)
  data = "WTechPass122"
  dk = fernet.ecrypt(data.encode)
  return dk.decode()
