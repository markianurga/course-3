# напиши здесь код создания и управления картой
class Mapmanager:
    def __init__ (self):
        self.model = 'block'
        self.texture = 'stone.png'
        self.startNew()
        self.addblock((1,4,1))    
        self.addblock((0,4,-1))
    def addblock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture( loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
    def startNew (self):
        self.land = render.attachNewNode("land")
        