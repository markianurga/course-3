# напиши тут код основного вікна гри
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager


class Game(ShowBase):
    def __init__ (self):
        super().__init__()
        self.land = Mapmanager()
        base.camLens.setFov(90)



ret = Game() 
ret.run()
