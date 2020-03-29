def urlify(string,length):
    for i in range(string.count(" ")*2):
        string.append(" ")
    j = len(string)-1
    print(j)
    for i in range(length,0,-1):
        print(string[i])
        if(string[i]!=' '):
            string[j] = string[i]
            j-=1
        else:
            string[j] = '0'
            string[j-1] = '2'
            string[j-2] = '%'
            j-=3
    print (string)
    return "".join(string)

url = 'Hel l o'
print("["+url.rstrip()+"]")
print(urlify(list(url), 6))