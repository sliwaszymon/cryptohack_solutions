# first step: pip install PyCryptodome
# pycryptodome==3.11.0

# need to remember, 2 usefull methods:
# Crypto.Util.number.long_to_bytes()
# Crypto.Util.number.bytes_to_long()

import Crypto.Util.number
integer_msg = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
decoded = Crypto.Util.number.long_to_bytes(integer_msg)
print(decoded)
# flag: crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}