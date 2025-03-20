class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def check_valid(self, new_catchphrase):
        for char in new_catchphrase:
            import string
            if char in string.punctuation:
                return False
        return True
    
    def check_item(self, item):
        valid_items = set(["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"])
        return item in valid_items
    
    def set_catchphrase(self, new_catchphrase):
        if self.check_valid(new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")
    
    def add_item(self, item_name):
        if self.check_item(item_name):
            self.furniture.append(item_name)

'''
bones = Villager("Bones", "Dog", "yip yip")
print(bones.name, bones.species, bones.catchphrase, bones.furniture)

bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))
'''

alice = Villager("Alice", "Koala", "guvnor")
alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)