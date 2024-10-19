# напиши тут код основного вікна гри
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__ (self):
        super().__init__()
        self.land = Mapmanager()
        self.land.loadLand('m5/u3/2/land.txt')
        self.hero = Hero((0,0,4),self.land)
        base.camLens.setFov(90)
        



ret = Game() 
ret.run()
