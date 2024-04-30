str = "AGK1LAU45ZTM126IKL"
# str="CLE35QGK125ZKA1125UK"
vowels = "aeiouAEIOU"
temp = ''
sum=0
for i in range(len(str)):
    if str[i].isnumeric():
        if str[i-1].isalpha():
            x=i-1
        temp += str[i]
    elif temp:
        # print(temp)
        if str[i] in vowels or str[x] not in vowels:
            sum=sum+int(temp)
            print(temp)
        temp=''
print(sum)