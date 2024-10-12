# напиши тут код основного вікна гри
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager


class Game(ShowBase):
    def __init__ (self):
        super().__init__()
        self.land = Mapmanager()
        self.land.loadLand('m5/u3/2/land3.txt')
        base.camLens.setFov(90)
        



ret = Game() 
ret.run()
