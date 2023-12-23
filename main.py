class System:
    def __init__(self, name, price, library_size):
        self.name = name
        self.price = price
        self.library_size = library_size
    
    def has_shinobi(self):
        return 'Yes'

class MarkIII(System):
    def __init__(self, name, price, library_size):
        super().__init__(name, price, library_size)

class GameGear(System):
    def __init__(self, name, price, library_size):
        super().__init__(name, price, library_size)

class Genesis(System):
    def __init__(self, name, price, library_size):
        super().__init__(name, price, library_size)

class ThirtyTwoX(System):
    def __init__(self, name, price, library_size):
        super().__init__(name, price, library_size)
    def has_shinobi(self):
        return 'No'

class SG1000(System):
    def __init__(self, name, price, library_size):
        super().__init__(name, price, library_size)
        
    def has_shinobi(self):
        return 'No'


sg1000 = SG1000('Mark I', 140, 76)
base = Genesis('Model2', 150, 600)
addon = ThirtyTwoX('32X', 120, 24)
towerofpower = System('Genesis32XCD', 270, 624)
print('Did ' + str(addon.name) + ' have Shinobi? ' + addon.has_shinobi())
print('Did ' + str(towerofpower.name) + ' have Shinobi? ' + towerofpower.has_shinobi())
