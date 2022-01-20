from PIL import Image, ImageChops

lemur = Image.open('general/xor/Lemur_XOR/lemur.png')
flag = Image.open('general/xor/Lemur_XOR/flag.png')

ImageChops.difference(lemur, flag).show()

# crypto{X0Rly_n0t!}