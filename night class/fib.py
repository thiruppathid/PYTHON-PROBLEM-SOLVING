class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def fibonacci_linked_list(n):
    # Initialize the linked list with the first two Fibonacci numbers
    head = Node(0)
    temp=head
    temp.next = Node(1)
    current = head.next
    #temp=head

    # Generate the remaining Fibonacci numbers
    for _ in range(n - 2):
        next_fib = current.data + temp.data
        current.next = Node(next_fib)
        current = current.next
        temp = temp.next

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

n = 10  # Number of Fibonacci numbers to generate
fibonacci_head = fibonacci_linked_list(n)
print("Fibonacci series with", n, "elements:")
print_linked_list(fibonacci_head)
