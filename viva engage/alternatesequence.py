def alternate(string):
    l=0
    r=len(string)-1
    string=list(string)
    while l<=r:
        string[l],string[r]=string[r],string[l]
        l+=1
        r-=1
    string=''.join(string)
    print(string)
string=input()
alternate(string)
#Prosoccer