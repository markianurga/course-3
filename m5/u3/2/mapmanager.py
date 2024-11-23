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
        self.block.setTag("at", str(position))
        self.block.reparentTo(self.land)
    def findBloks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))
    def findghestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)
        
        
    def isEmpty(self, pos):
        bloks = self.findBloks(pos)
        if bloks:
            return False
        else:
            return True
        
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
                
    def delblock(self, pos):
        blocks = self.findBloks(pos)
        print(543)
        for block in blocks:
            block.removeNode()
            
    def bildblock(self, pos):
        x,y,z = pos
        nu = self.findghestEmpty(pos)
        if nu[2] <= z+1:
            self.addblock(nu)
            
    def delblockfrom(self, pos):
        x,y,z = self.findghestEmpty(pos)
        pos1 = x,y,z-1
        self.delblock(pos1)