from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):
    def __init__ (self):
        super().__init__()
        self.model = loader.loadModel('Barn')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
        self.model2 = loader.loadModel('sword')
        self.model2.reparentTo(render)
#        self.model2.setScale(0.1)
        self.model2.setPos(4, 30, -3)


ret = Game() 
ret.run()
