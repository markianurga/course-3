# напиши тут код створення та управління карткою
class Mapmanager:
    def __init__ (self):
        self.model = 'block'
        self.texture = 'stone.png'
        self.startNew()
#        self.addblock((1,4,1))    
#        self.addblock((0,4,-1))
    def addblock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture( loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
    def startNew (self):
        self.land = render.attachNewNode("land")
    def loadLand(self, filename):
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        self.addblock((x, y, z0))
                    x = x + 1
                y = y + 1
