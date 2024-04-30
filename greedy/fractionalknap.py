profits = []
for i in range(7):
    x, y = map(int, input().split())
    profits.append([x, y, x / y])

sorted_ele = sorted(profits, key=lambda x: x[-1], reverse=True)
print(sorted_ele)
profits_stack = []
bag_value = 15
bag_stack=[]
for pro, wt, val in sorted_ele:
    if bag_value != 0:
        if bag_value - wt < 0:
            profits_stack.append((bag_value / wt) * pro)  
            bag_value -= bag_value
            bag_stack.append(bag_value)
        else:
            bag_value -= wt
            bag_stack.append(bag_value)
            profits_stack.append(pro)

print(bag_stack)


print(profits_stack)
print(sum(profits_stack))

