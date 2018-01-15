def main():
    plainText= "sshzssfryvkeeghdihgkciidpvpiyvbpyvnnawlvtevhamsu"
    str_result =""
    m = [[45,-18],[-27,63]]
    print(len(m))
    for i in range (0,len(plainText),len(m)):
        l = []
        l.append(ord(plainText[i])-ord('a'))
        print(plainText[i],end='')
        if i+1 == len(plainText):
            l.append(ord('a')-ord('a'))
            print('a')
        else:
            l.append(ord(plainText[i+1])-ord('a'))
            print(plainText[i+1])
        print(l)
    # do matrix multiplication
        result=[]
        for i in range(0,len(m)):
            elt = 0
            for j in range(0,len(m)):
                elt= elt+m[j][i]*l[j]
            result.append(elt)
        print(result) 
        result[0]=result[0]%26
        result[1] = result[1]%26
        print(result)
        print(chr(result[0]+ord('a'))+chr(result[1]+ord('a')))
        str_result =str_result+ chr(result[0]+ord('a')) +chr(result[1]+ord('a'))
        print(str_result)

if __name__ == '__main__':
    main()