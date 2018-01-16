key_and_inverse = {1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}

def convertLetter(character, a,b):
    return chr((((ord(character)-ord('a'))-b)%26*key_and_inverse[a])%26+ord('a'))

def modeOfVector(vector):
    mode = 0
    for k in vector:
        mode = mode + vector[k]**2
    mode = mode**(1/2)
    return mode

def calculateFrequency(text,starting_pos,step_len):
    words_frequency = {}
    count = 0
    for i in range(0, 26):
        words_frequency[chr(ord('a') + i)] = 0
    for i in range(starting_pos, len(text), step_len):
        words_frequency[text[i]] = words_frequency[text[i]] + 1
        count = count+1
    for k in words_frequency:
        words_frequency[k] = words_frequency[k] / count
    return words_frequency

def guessKey(text):
    std_english_frequency_dict = {'a':0.08167,'b':0.01492,'c':0.02782,'d':0.04253,'e':0.12702,'f':0.02228,'g':0.02015,'h':0.06094,'i':0.06966,'j':0.00153,'k':0.00772,'l':0.04025,'m':0.02406,'n':0.06749,'o':0.07507,'p':0.01929,'q':0.00095,'r':0.05987,'s':0.06327,'t':0.0905,'u':0.02758,'v':0.00978,'w':0.0236,'x':0.00150,'y':0.01974,'z':0.00074}
    modeOfStdEnglish = modeOfVector(std_english_frequency_dict)
    max_cosine = 0
    max_a = 0
    max_b = 0
    for i in range(0,26):
        for a in key_and_inverse:
            plaintext = ''
            for j in range(0,len(text)):
                plaintext = plaintext+convertLetter(text[j],a,i)
            frequency_of_text = calculateFrequency(plaintext,0,1)
            modeOfText = modeOfVector(frequency_of_text)
            dotProduct = 0
            for key in frequency_of_text:
                dotProduct = dotProduct+ frequency_of_text[key]*std_english_frequency_dict[key]
            if dotProduct/modeOfStdEnglish/modeOfText > max_cosine:
                max_cosine = dotProduct/modeOfStdEnglish/modeOfText
                max_a = a
                max_b = i
    
    return max_a,max_b

if  __name__ == '__main__':
    cipher_text = 'kqerejebcppcjcrkieacuzbkrvpkrbcibqcarbjcvfcupkriofkpacuz'\
                    'qepbkrxpeiieabdkpbcpfcdccafieabdkpbcpfeqpkazbkrhaibkap'\
                    'cciburccdkdccjcidfuixpafferbiczdfkabicbbenefcupjcvkabp'\
                    'cydccdpkbcocperkivkscpicbrkijpkabi'
    a,b =guessKey(cipher_text)
    plaintext = ''
    for i in range(0,len(cipher_text)):
        plaintext = plaintext+convertLetter(cipher_text[i],a,b)
    print(str(a)+"  "+str(b))
    print(plaintext)