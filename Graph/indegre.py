from collections import defaultdict
add_list=defaultdict(list)
#7
#13
ver=int(input())
ed=int(input())
for i in range(ed):
    u,v=map(int,input().split())
    add_list[u].append(v)
print(add_list)
def indegre(add_list):
    ind_deg=[0]*ver
    out_deg=[0]*ver
    for i in range(ver):
        out_deg[i]=len(add_list[i])
        for j in add_list[i]:
            ind_deg[j]+=1
    for i in range(ver):
        print(i," ",out_deg[i]," ",ind_deg[i])
