

class Pokemon:
    
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught


name_dict = {1: 'bulbasaur', 2:'ivysaur', 3:'venusaur', 4:'charmander', 5:'charmeleon', 6:'charizard', 7:'squirtle'}


bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass & Poison',
  'For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.',
  True)

charmander = Pokemon(4, 'Charmander', 'Fire', 
    'The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.',
    False)

squirtle = Pokemon(7, 'Squirtle', 'Water',
    'After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.',
    True)