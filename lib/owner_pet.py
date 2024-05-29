class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]

    def __init__(self,name,pet_type, owner = None ):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("pet must be in pet types")
        self.name = name
        self.owner = None
        self.pet_type = pet_type
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("owner must be instance of Owner")
            self.owner = owner
            owner.add_pet(self)        
        Pet.all.append(self)


    

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise Exception("pet must be a instance of Pet")
        self._pets.append(pet)
        pet.owner = self
        
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

