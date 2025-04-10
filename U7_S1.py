def count_layers(sandwich):
    if len(sandwich) == 1:
        return 1

    return 1 + count_layers(sandwich[1])

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

sandwich3 = ["bread", ["lettuce"]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))


def reverse_orders(orders):
    arr = orders.split(" ")
    # print(arr)
    if len(arr) == 1:
        return arr[0]
    
    return arr[-1] + " " + reverse_orders(arr_to_string(arr[0:len(arr)-1]))

def arr_to_string(arr):
    delimiter = " "
    return delimiter.join(arr)
    
print(reverse_orders("Bagel Sandwich Coffee"))

def can_split_coffee(coffee, n): # return bool
    return coffee_helper(coffee) % n == 0

def coffee_helper(arr): #sum up list recursively
    if len(arr) == 1:
        return arr[0]

    return arr[0] * coffee_helper(arr[1:])


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
'''
[5,10,15] , 4
5 * [10, 15] , 4
5 * 10 * [15] , 4
5 * 10 * 15 , 4  -->  750
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

'''
two pointer
which ever one hit the null first, then end it -> link it with the other one
'''
def merge_orders(sandwich_a, sandwich_b):
    pass