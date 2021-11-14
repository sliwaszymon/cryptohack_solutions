import base64
hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytes_from_hex = bytes.fromhex(hex)
print(bytes_from_hex)
decoded = base64.b64encode(bytes_from_hex)
print(decoded)

# flag: crypto/Base+64+Encoding+is+Web+Safe/