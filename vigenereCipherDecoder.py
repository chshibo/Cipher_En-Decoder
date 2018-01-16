def translateToPlainText(cipher_text,key):
    result = ''
    offset = 0
    for i in range(0,len(cipher_text)):
        result = result+ chr(((ord(cipher_text[i])-ord('a'))-(ord(key[offset])-ord('a')))%26+ord('a'))
        offset = (offset+1)%len(key)
    return result

def convertLetter(character, key):
    return chr(((ord(character)-ord('a'))-(ord(key)-ord('a')))%26+ord('a'))

def modeOfVector(vector):
    mode = 0
    for k in vector:
        mode = mode + vector[k]**2
    mode = mode**(1/2)
    return mode

def guessTheLetter(text):
    std_english_frequency_dict = {'a':0.08167,'b':0.01492,'c':0.02782,'d':0.04253,'e':0.12702,'f':0.02228,'g':0.02015,'h':0.06094,'i':0.06966,'j':0.00153,'k':0.00772,'l':0.04025,'m':0.02406,'n':0.06749,'o':0.07507,'p':0.01929,'q':0.00095,'r':0.05987,'s':0.06327,'t':0.0905,'u':0.02758,'v':0.00978,'w':0.0236,'x':0.00150,'y':0.01974,'z':0.00074}
    modeOfStdEnglish = modeOfVector(std_english_frequency_dict)
    cosineOfGuesses = {}
    for i in range(0,26):
        plaintext = ''
        for j in range(0,len(text)):
            plaintext = plaintext+convertLetter(text[j],chr(ord('a')+i))
        frequency_of_text = calculateFrequency(plaintext,0,1)
        modeOfText = modeOfVector(frequency_of_text)
        dotProduct = 0
        for k in frequency_of_text:
            dotProduct = dotProduct+ frequency_of_text[k]*std_english_frequency_dict[k]
        cosineOfGuesses[i] = dotProduct/modeOfStdEnglish/modeOfText
    max_key = 1
    max_cosine = cosineOfGuesses[1]
    for k in cosineOfGuesses:
        if(cosineOfGuesses[k]>max_cosine):
            max_cosine = cosineOfGuesses[k]
            max_key = k
    return chr(max_key+ord('a'))

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

def calculateCoincidenceIndex(frequency):
    index = 0
    for key in frequency:
        index = index + frequency[key]**2
    return index

def main():
    cipher_text = 'hlfiusvsaqfpfpwaryxewdudwbrvxvrthapcjlhrlalbkwfeecmlpfvuyimxqpiovczogidthjg'\
        'dhrlifyxkwhuigkullqqqhltvyzckbseelxrpikavbrxmysirovgipszwxpiwyauszeuiqhglxe'\
        'sombmhuepeyplvxoethjysytwfydbxndutimvhtzjzzazwiigktqzqpsfpeijyuklfrgnpfecko'\
        'huevmwnoiihvogamphbdseiymsogvasyfzvthckoueifegzoqbvrmhyysqembrvxvnecpirnmih'\
        'wttwtmaooirmyoqbzylszwqembrvxvnqcklalsxpkthswzhnmewtfvxohsbrlmycwfrchjkthti'\
        'frhhyxpmxvrorbrlthdcdghxvjlllnsiekckfhbzoyifijeuklsfpxgnlfigkuegiapljgvlphw'\
        'lpnpcquagyuayopoadhjrpneihvtkivfcomgnsmvtyajwfnlivnywfxzrthtwppbvhzeyvtxxbt'\
        'woekeypfvahrpimsrckbcghxwycybboadfiysiaqqnlecpyizswagiitafbavntlskqnembvavg'\
        'tfhqqhuizlytgbbctemxtdyxigfohrfdczibghbwndgvaiosmmyfnbncepbwyzfxvroaepbtnei'\
        'duiesxzjeqqnlyptflfavpamsyslleguifwjwzrxcahbwxhiolwdubiywsqiyrthxmpmeqdghxv'\
        'jtmkwhuigkxflmzwfigknyneqgvfmljjvrbyaepmylfjwggaeprphfvhuebvipaomsfofiytgbw'\
        'fbtaiwnbbzwfhoiwjhbifyymljdujmtreemsrmqwknrwwysylksnnpmysgbbvrrxrthcpgchrbr'\
        'xffxzqvtrskebbuoahtxyzypjsytxhwzoklplwaewgypigvnwmfycptsfbrgtcuizsrflgtxgbz'\
        'qrsnvwzoklgvtpmysbbzghryvnrbqibqlxjyebbaheexxxeuhmmbupeypltifqimwjinomardha'\
        'seitvwftaiglnqmflwaiwpneihaoupjxiimwfwtwmpxygknvxwfyxzwcyewfdmlbmnrsplnnbxn'\
        'sjhhywdjomjvonwbplbwigoywnrbqwtyaghqzihihghxgwzqaacswtxjcaxhsesmljcy'
    coincidence_index_bundle = {}
    for i in range(1,15):
        coincidence_index_single = 0
        for j in range(0,i):
            coincidence_index_single = coincidence_index_single +calculateCoincidenceIndex(calculateFrequency(cipher_text,j,i))
        coincidence_index_bundle[i] = coincidence_index_single/i
    max_coin = coincidence_index_bundle[1]
    max_len = 1
    for i in range(1,15):
        if coincidence_index_bundle[i] > max_coin:
            max_coin = coincidence_index_bundle[i]
            max_len = i
    key = ''
    for i in range(0,max_len):
        chunk_text = ''
        for j in range(i,len(cipher_text),max_len):
            chunk_text = chunk_text + cipher_text[j]
        key = key+guessTheLetter(chunk_text)
    print(key)
    print(translateToPlainText(cipher_text,key))

if  __name__ == '__main__':
    main()