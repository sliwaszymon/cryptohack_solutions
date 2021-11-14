# first step: pip install pwntools
# pwntools==4.6.0

from pwnlib.util.fiddling import xor

k1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2k3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flagk1k2k3 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag = xor(flagk1k2k3, k2k3, k1)
print(flag)

# flag: crypto{x0r_i5_ass0c1at1v3}