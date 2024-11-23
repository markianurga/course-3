# напиши свій код тут
class Hero:
    def __init__(self, pos , land):
        self.mode = True
        self.land = land
        self.model =  loader.loadModel('ant')
        self.model.reparentTo(render)
        self.model.setPos(pos)
        self.model.setH(180)
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
        base.accept('z',self.changeMode)
        
        base.accept('f',self.build)
        base.accept('b',self.destroy)
        base.accept('c',self.changeView)
        base.accept('e',self.turn_right)
        base.accept('q',self.turn_left)
        base.accept('e-repeat',self.turn_right)
        base.accept('q-repeat',self.turn_left)
        base.accept('w',self.forward)
        base.accept('a',self.left)
        base.accept('s',self.back)
        base.accept('d',self.right)
        base.accept('w-repeat',self.forward)
        base.accept('a-repeat',self.left)
        base.accept('s-repeat',self.back)
        base.accept('d-repeat',self.right)
        base.accept('space',self.up)
        base.accept('shift',self.down)
        base.accept('space-repeat',self.up)
        base.accept('shift-repeat',self.down)
    
    def up(self):
        self.model.setZ(self.model.getZ( )+1)
    def down(self):
        self.model.setZ(self.model.getZ( )-1)
    def forward(self):
        angle = (self.model.getH() + 180) % 360
        self.move_to(angle)
    def back(self):
        angle = (self.model.getH() + 0) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.model.getH() + 270) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.model.getH() + 90) % 360
        self.move_to(angle) 
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
        pos = self.look_at(angle)
        self.model.setPos(pos)
    
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findghestEmpty(pos)
            self.model.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] +1
            if self.land.isEmpty(pos):
                self.model.setPos(pos)

    
    def look_at(self, angle):
        x = self.model.getX()
        x = round(x)
        y = self.model.getY()
        y = round(y)
        z = self.model.getZ()
        z = round(z)
        
        dx, dy = self.check_dir(angle)
        
        return x + dx, y + dy, z
    
    def check_dir(self, angle):
        if 0 <= angle < 20:
            return 0, -1
        elif 20 <= angle < 65:
            return 1, -1
        elif 65 <= angle < 110:
            return 1, 0
        elif 110 <= angle < 155:
            return 1, 1
        elif 155 <= angle < 200:
            return 0, 1
        elif 200 <= angle < 240:
            return -1, 1
        elif 240 <= angle < 290:
            return -1, 0
        elif 290 <= angle < 335:
            return -1, -1
        elif 335 <= angle <= 360:
            return 0, -1
        
    
    def move_to(self, angle):
        if self.mode == True:
            self.just_move(angle)
        else:
            self.try_move(angle)
    
    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True
            
    def build(self):
        angle = self.model.getH()%360
        pos = self.look_at(angle)
        if self.mode == True:
            self.land.addblock(pos)
        else:
            self.land.bildblock(pos)
    
    def destroy(self):
        angle = self.model.getH()%360
        pos = self.look_at(angle)
        print(999)
        if self.mode == True:
            self.land.delblock(pos)
        else:
            self.land.delblockfrom(pos)
    
    