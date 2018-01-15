def main():
    palin_text = "cryptographic"
    key = "eng"
    result = ''
    offset = 0
    for i in range(0,len(palin_text)):
        result = result+ chr(((ord(palin_text[i])-ord('a'))+(ord(key[offset])-ord('a')))%26+ord('a'))
        offset = (offset+1)%len(key)
    print(result)
        

if __name__ == '__main__':
    main()