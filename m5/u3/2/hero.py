# напиши свій код тут
class Hero:
    def __init__(self, pos , land):
        self.mode = True
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
        base.accept('e',self.turn_right)
        base.accept('q',self.turn_left)
        base.accept('e-repeat',self.turn_right)
        base.accept('q-repeat',self.turn_left)
#        base.accept('w',self.changeView)
#        base.accept('a',self.changeView)
#        base.accept('s',self.changeView)
#        base.accept('d',self.changeView)
        
        
    def changeView(self):  
        if self.comeraOn:
            self.cameraAp()
        else:
            self.camerabind()
        
        
    def turn_left(self):
        q = self.model.getH()
        q = q + 5
        self.model.setH(q)
        
        
    def turn_right(self):
        q = self.model.getH()
        q = q - 5
        self.model.setH(q)
        
    
    def just_move(self, angle):
        pass
    
    def try_move(self, angle):
        pass
    
    def look_at(self, angle):
        pass
    
    def check_dir(self, angle):
        pass
    
    def move_to(self, angle):
        if self.mode == True:
            self.just_move(angle)
        else:
            self.try_move(angle)
    
