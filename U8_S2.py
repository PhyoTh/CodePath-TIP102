'''
Problem 1: Sorting Plants by Rarity
You are going to a plant swap where you can exchange cuttings of your plants for new plants from other plant enthusiasts. 
You want to bring a mix of cuttings from both common and rare plants in your collection. You track your plant collection in a binary search tree (BST) where each node has a key and a val. The val contains the plant name, and the key is an integer representing the plant's rarity. Plants are organized in the BST by their key.

To help choose which plants to bring, write a function sort_plants() which takes in the BST root collection and returns an array of plant nodes as tuples in the form (key, val) sorted from least to most rare. Sorted order can be achieved by performing an inorder traversal of the BST.
'''
from collections import deque

# class TreeNode:
#     def __init__(self, val, key, left=None, right=None):
#         self.key = key      # Plant price
#         self.val = val      # Plant name
#         self.left = left
#         self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
        
# def sort_plants(collection): # return a list
#     res = []
    
#     def helper(collection): # return the a tuple
#         if not collection:
#             return 
#         helper(collection.left)
#         res.append((collection.key, collection.val))
#         helper(collection.right)
    
#     helper(collection)
#     return res

# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))

'''
Problem 2: Flower Finding
You are looking to buy a new flower plant for your garden.
The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store.
The plants are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name,
write a function find_flower() that returns True if the flower is present in the garden and False otherwise.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val              
        self.left = left
        self.right = right
        
def find_flower(inventory, name): # return bool 
    # Base Case
    if not inventory:
        return False
    
    # Recursive Call
    if name < inventory.val:
        return find_flower(inventory.left, name)
    elif name == inventory.val:
        return True
    else:
        return find_flower(inventory.right, name)
    
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 