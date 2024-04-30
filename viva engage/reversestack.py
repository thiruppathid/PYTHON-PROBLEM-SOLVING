def reverse_stack(stack):
    if not stack:  
        return

    bottom = remove_bottom(stack)
    reverse_stack(stack)
    stack.append(bottom)

def remove_bottom(stack):
    top = stack.pop() 

    if not stack:  
        return top

    bottom = remove_bottom(stack)

    stack.append(top)

    return bottom

stack = [1, 2, 3, 4]
print("Original stack:", stack)

reverse_stack(stack)

print("Reversed stack:", stack)
