def calculateFrequency(text,starting_pos,step_len):
    words_frequency = {}
    for i in range(0, 26):
        words_frequency[chr(ord('a') + i)] = 0
    for i in range(starting_pos, len(text), step_len):
        words_frequency[text[i]] = words_frequency[text[i]] + 1
    for k in words_frequency:
        words_frequency[k] = words_frequency[k] / len(text)
    return words_frequency


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
    words_frequency = calculateFrequency(cipher_text,0,1)
    for i in range(0,15):
        coincidence_index_single = 0
        for i in range(0,i):


if __name__ == '__main__':
    main()
