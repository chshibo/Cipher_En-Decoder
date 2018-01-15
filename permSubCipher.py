import operator
def main():
    cipher_text = 'emglosudcgdncuswysfhnsfcykdpumlwgyicoxysipjckqpkugkmgolicgincgacksnisacykzsckxecjckshysxcgoidpkzcnkshicgiwygkkgkgoldsilkgoiusigledspwzugfzccndgyysfuszcnxeojncgyeoweupxezgacgnfglknsacigoiyckxcjuciuzcfzccndgyysfeuekuzcsocfzccnciaczejncshfzejzegmxcyhcjumgkucy'
    alpha_count = {}
    for i in range(0,26):
        alpha_count[chr(ord('a')+i)]=0
    for i in range(0,len(cipher_text)):
        alpha_count[cipher_text[i]] = alpha_count[cipher_text[i]]+1
    for key in alpha_count:
        alpha_count[key] = alpha_count[key]/len(cipher_text)
    for key,value in sorted(alpha_count.items(), key=operator.itemgetter(1),reverse=True):
        print(str(key)+" : "+str(value))
    substitute = {'c':'t','y':'l'}
    plain_text = ''
    for i in range(0,len(cipher_text)):
        if cipher_text[i] in substitute:
            plain_text = plain_text+substitute[cipher_text[i]]
        else:
            plain_text = plain_text+ cipher_text[i]
    print (cipher_text)
    print(plain_text)

if __name__ == '__main__':
    main()
