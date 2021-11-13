dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dict = [x for x in dict]
def decrypt(text):
    text = text.split(' ')
    for combination in range(1,len(dict),1):
        decoded = []
        for word in text:
            new_word = ''
            for letter in word:
                index = dict.index(letter)-combination
                if index < 0:
                    index = len(dict)+index
                new_word += dict[index]
            decoded.append(new_word)
        print(' '.join(decoded))

decrypt("PSZZCP BSQR NMJYP NMJGAC")

# now needs to find phrazes looking like true password
# RUBBER DUST POLAR POLICE