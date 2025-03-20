# Problem 2: Identifying Endangered Species

from collections import Counter
def count_endangered_species(endangered_species, observed_species):
    endangered = set(endangered_species)
    observed = Counter(observed_species)
    count = 0
    
    for species in endangered:
        count += observed.get(species, 0)
        
    return count