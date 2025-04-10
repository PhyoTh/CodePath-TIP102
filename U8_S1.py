class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_vine(root):
    if root is None:
        return []
    return [root.val] + right_vine(root.right)

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)
print(right_vine(ivy1))
print(right_vine(ivy2))

def it_right_vine(root):
    curr = root
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.right
    return res


ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)
print(it_right_vine(ivy1))

def survey_tree(root):
    if root is None:
        return []
    return survey_tree(root.left) + survey_tree(root.right) + [root.val]

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))


def sum_inventory(inventory):
    if inventory is None:
        return 0
    return sum_inventory(inventory.left) + sum_inventory(inventory.right) + inventory.val

inventory = TreeNode(
    40, TreeNode(5, TreeNode(20)), TreeNode(10, TreeNode(1), TreeNode(30))
)

print(sum_inventory(inventory))


# def calculate_yield(root):
#     if root.val == "+":
#         return calculate_yield(root.left) + calculate_yield(root.right)
#     if root.val == "-":
#         return calculate_yield(root.left) - calculate_yield(root.right)
#     map("-")

def calculate_yield_2(root):
    if root is None:
        return None
    if isinstance(root.val, int):
        return str(root.val)
    return str(eval(calculate_yield_2(root.left) + root.val + calculate_yield_2(root.right)))

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield_2(root))


def get_most_specific(taxonomy):
    if taxonomy.right == None and taxonomy.left == None:
        return [taxonomy.val]
    return get_most_specific(taxonomy.left) + get_most_specific(taxonomy.right)

plant_taxonomy = TreeNode(
    "Plantae",
    TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
    TreeNode(
        "Flowering",
        TreeNode("Gymnosperms"),
        TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots")),
    ),
)

print(get_most_specific(plant_taxonomy))
