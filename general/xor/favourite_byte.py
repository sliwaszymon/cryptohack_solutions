from pwnlib.util.fiddling import xor

data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_from_data = bytes.fromhex(data)

potecial_flags = []
for x in range(256):
    byte_done = b''
    for bytex in bytes_from_data:
        byte_done += xor(bytex, x)
    try:
        potecial_flags.append(byte_done.decode("utf-8"))
    except:
        potecial_flags.append("niedekodowalne")

print(''.join([flag for flag in potecial_flags if "crypto" in flag]))

# flag: crypto{0x10_15_my_f4v0ur173_by7e}