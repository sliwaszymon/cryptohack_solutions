# first step: pip install pwntools
# pwntools==4.6.0

from pwnlib.util.fiddling import xor

text = 'label'
integer = int(13)
letters = [ord(x) for x in text]
new_letters = []
for x in letters: 
    new_letters.append(str(xor(x, integer)).replace("b'","").replace("'",""))

print(''.join(new_letters))

# flag: crypto{aloha}