class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front == None and self.rear == None

    '''
    Accepts a tuple of two strings (song, artist) 
    and adds the element with the specified tuple to the end of the queue.
    '''
    def enqueue(self, item):
        newNode = Node(item)

        if self.is_empty(): # empty queue
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    '''
    Removes and returns the element at the front of the queue. If the queue is empty, returns None.
    '''
    def dequeue(self):
        if self.is_empty():
            return
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.value
    
    '''
    Returns the value of the element at 
    the front of the queue without removing it. If the queue is empty, returns None.
    '''
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.value
        
# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 