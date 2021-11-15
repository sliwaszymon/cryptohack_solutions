# first step: pip install pwntools
# pwntools==4.6.0

from pwnlib.util.fiddling import xor

text = 'label'
integer = int(13)
letters = [str(xor(ord(x), integer)).replace("b'","").replace("'","") for x in text]

print(''.join(letters))

# flag: crypto{aloha}