# напиши свій код тут
class Hero:
    def __init__(self, pos , land):
        self.land = land
        self.model =  loader.loadModel('ant')
        self.model.reparentTo(render)
        self.model.setPos(pos)
        self.model.setScale(0.66)
        
        self.camerabind()
        self.accept_events()
        
        
    def camerabind (self):
        base.disableMouse()
        base.camera.reparentTo(self.model)
#       base.camera.setPos()
        self.comeraOn = True
    
    def cameraAp(self):
        base.enableMouse()
        base.camera.reparentTo(render)
        xyz = self.model.getPos()
        base.mouseInterfaceNode.setPos(xyz)
        
        
        self.comeraOn = False

       
    def accept_events(self):
        base.accept('c',self.changeView)
        
        
    def changeView(self):  
        if self.comeraOn:
            self.cameraAp()
        else:
            self.camerabind()
        
        
        
        
        