import js as p5
game_state = 'Prepare'
invaderfont = p5.loadFont('PressStart2P-Regular.ttf')
heart = p5.loadImage('Heart.png')  
star_counter = 0
wave = p5.loadImage('wave.png')  

print("left and right arrow to move horizontally, Up and donw arrow to move vertically, Collet 10 stars to win the game")

class Background:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.background = p5.loadImage('Background.png')
 
  def draw(self):
    p5.push()
    p5.image(self.background, self.x, self.y,300,300)
    p5.imageMode(p5.CENTER)  
    p5.pop()

class UFO:
  def __init__(self, x=150, y=150):
    self.x = x
    self.y = y
    self.UFO = p5.loadImage('UFO.png')
    self.Explosion = p5.loadImage('Explosion.png')
    self.speed = 1
    self.hit_counter = 0  # how many times UFO was hit
    self.state = 'normal'
    self.hit_timer = 0 


  def update(self):
    if p5.keyCode == p5.RIGHT_ARROW:
      if self.x < 300:
          self.x += self.speed
    elif p5.keyCode == p5.LEFT_ARROW:
      if self.x > -0:
          self.x -= self.speed
    if p5.keyCode == p5.UP_ARROW:
      if self.y > -0:  
          self.y -= self.speed
    elif p5.keyCode == p5.DOWN_ARROW:
      if self.y < 300: 
          self.y += self.speed

  def draw(self):
    p5.push()
    p5.imageMode(p5.CENTER)  
    p5.translate(self.x, self.y) 
    p5.rotate(p5.radians(0))
    if(self.state == 'normal'):
      p5.image(self.UFO, 0, 0, 40, 30)
    elif(self.state == 'hit'):
      # draw the exploded UFO here..
      # p5.image(self.explosion_image, 0, 0, 30, 30)
      p5.fill(255, 0, 0)
      # p5.image(self.explosion, 0, 0, 30, 30)
      p5.image(self.Explosion, 0, 0, 50, 50)
      print(self.hit_counter)
      # 2 seconds passed after hit:
      if(p5.millis() > self.hit_timer + 2000):
        self.state = 'normal'
      
    p5.pop()





class laser_Right:
  INACTIVE = 0
  PREPARING = 1
  FIRING = 2

  def __init__(self, x=0):
    self.x = x
    self.y = p5.random(0, p5.height)
    self.speed = p5.random(0.5, 2)
    self.direction = 1
    self.laser_inactive = p5.loadImage('Laser1.png')
    self.laser_preparing = p5.loadImage('Laser2.png')
    self.laser_firing = p5.loadImage('Laser3.png')
    self.state = self.INACTIVE
    self.fire_time = p5.random(1000, 5000)  
    self.last_update_time = p5.millis()  

  def update(self):
    self.y += self.speed * self.direction
    if self.y > p5.height-40 or self.y < -10:
      self.direction *= -1

    current_time = p5.millis()
    if (self.state == self.INACTIVE) and (current_time - self.last_update_time) > self.fire_time:
      self.state = self.PREPARING
      self.fire_time = 1000  
      self.last_update_time = current_time
    elif (self.state == self.PREPARING) and (current_time - self.last_update_time) > self.fire_time:
      self.state = self.FIRING
      self.fire_time = 1000  
      self.last_update_time = current_time
    elif (self.state == self.FIRING) and (current_time - self.last_update_time) > self.fire_time:
      self.state = self.INACTIVE
      self.fire_time = p5.random(1000, 5000) 
      self.last_update_time = current_time

  def draw(self):
    laser_width = 20  
    laser_height = 60  

    if (self.state == self.INACTIVE):
        laser_image = self.laser_inactive
    elif (self.state == self.PREPARING):
        laser_image = self.laser_preparing
    else:
        laser_image = self.laser_firing
        laser_width = 300  

    p5.push()
    p5.translate(self.x, self.y)
    p5.image(laser_image, 0, 0, laser_width, laser_height)
    p5.pop()

class laser_Left(laser_Right):
  def draw(self):
    laser_width = 20
    laser_height = 60

    if (self.state == self.INACTIVE):
        laser_image = self.laser_inactive
    elif (self.state == self.PREPARING):
        laser_image = self.laser_preparing
    else:
        laser_image = self.laser_firing
        laser_width = 300  

    p5.push()
    translate_x = p5.width - laser_width / 2
    p5.translate(translate_x, self.y)
    p5.scale(-1, 1)  
    p5.imageMode(p5.CENTER);  
    p5.image(laser_image, 0, 0, laser_width, laser_height)
    p5.pop()

class Heart:
  def __init__(self, lives=5):
    self.lives = lives
    self.hearts = ['Heartimage'] * lives  
    self.heart_image = p5.loadImage('Heart.png')

  def lose_life(self):
    if self.lives > 0:
        self.lives -= 1
        self.hearts.pop()

  def draw(self):
    for i in range(len(self.hearts)):
      p5.image(self.heart_image, 10 + i*30, 10, 20, 20)


class Star:
  def __init__(self):
    self.star_image = p5.loadImage('Star1.png')
    self.show = False  
    self.x = 0
    self.y = 0
    self.timer = 0  

  def update(self):
    if not self.show and (p5.millis() - self.timer) > 5000:
      self.x = p5.random(0, p5.width)
      self.y = p5.random(50, p5.height-50)
      self.show = True
      self.timer = p5.millis()
    elif self.show and (p5.millis() - self.timer) > 10000:
      self.show = False
      self.timer = p5.millis()

  def draw(self):
    if self.show:
        p5.image(self.star_image, self.x, self.y, 40, 40)



bg = Background()
UFO = UFO()
laser1 = laser_Right()
laser2 = laser_Left()
heart_number = Heart()
star = Star() 




print('Assignment #7 (Final Project)')

def setup():
  p5.createCanvas(300, 300)  

def draw():
  global game_state, heat, star_counter, wave
  if (game_state == 'Prepare'):
    p5.push()
    p5.textFont(invaderfont)
    bg.draw()
    p5.translate(p5.width/2,  p5.height/2) 
    p5.textSize(24)  
    p5.fill(255)
    p5.textSize(20)
    p5.text("Stellar Escape",-140,0)
    p5.textSize(12)
    p5.text('press anywhere to start', -140, 30) 
    p5.textSize(6)
    p5.fill(255,255,0)
    p5.text('left and right arrow to move horizontally ', -130, 50) 
    p5.text('Up and donw arrow to move vertically ', -110, 60) 
    p5.text('Collet 5 stars to win the game ', -100, 70) 
    p5.pop()
    
    
    if (p5.mouseIsPressed == True):
      game_state = 'Play'

  if (game_state == 'Fail'):
    p5.push()
    p5.textFont(invaderfont)
    bg.draw()
    p5.translate(p5.width/2,  p5.height/2) 
    p5.textSize(24)  
    p5.fill(255)
    p5.textSize(20)
    p5.text("You Fail!",-90,0)
    p5.textSize(12)
    p5.text('press anywhere to restart', -150, 80) 
    p5.pop()
    p5.push()
    p5.imageMode(p5.CENTER)
    if(p5.millis() % 1000 < 500):
      p5.image(UFO.Explosion, UFO.x, UFO.y, 50, 50)
    else:
      p5.image(UFO.Explosion, UFO.x, UFO.y, 80, 80)
    p5.pop()
    
    if (p5.mouseIsPressed == True):
      game_state = 'Play'
      UFO.x = 150
      UFO.y = 150
      UFO.state = 'normal'
      UFO.hit_counter = 0
      star_counter = 0
      heart_number.lives = 5
      heart_number.hearts = ['Heart_A'] * 5
      star.show = False
      star.timer = p5.millis()
      


  if (game_state == 'Play'):
    bg.draw()
    UFO.update()
    UFO.draw()
    laser1.update()
    laser1.draw()
    laser2.update()
    laser2.draw()
    heart_number.draw()
    star.update()
    star.draw()

    
    if laser1.state == laser1.FIRING and int(laser1.y) == UFO.y:
      print('shot')
      UFO.hit_counter += 1  # increase hit counter
      UFO.state = 'hit'
      UFO.hit_timer = p5.millis()  # update UFO hit timer
      heart_number.lose_life()

    if laser2.state == laser2.FIRING and int(laser2.y) == UFO.y:
      print('shot')
      UFO.hit_counter += 1  # increase hit counter
      UFO.state = 'hit'
      UFO.hit_timer = p5.millis()  # update UFO hit timer
      heart_number.lose_life()
   

    if UFO.y < 50 or UFO.y > 250:
      UFO.hit_counter += 1  # increase hit counter
      UFO.state = 'hit'
      UFO.hit_timer = p5.millis()  # update UFO hit timer
      heart_number.lose_life()

    if star.show and p5.dist(UFO.x, UFO.y, star.x, star.y) < 25:
      star_counter += 1
      star.show = False  
      star.timer = p5.millis()  


    p5.push()
    p5.imageMode(p5.CENTER)
    p5.image(star.star_image, 265, 20, 20, 20) 
    p5.textFont(invaderfont)
    p5.fill(255)
    p5.text(str(star_counter), 280, 25)  
    p5.pop()
    
    if star_counter >= 5:
      game_state = 'You Win'
    
    
    if UFO.hit_counter == 5:
      game_state = 'Fail'

  if game_state == 'You Win':
    bg.draw()
    p5.push()
    p5.textFont(invaderfont)
    bg.draw()
    p5.translate(p5.width/2,  p5.height/2) 
    p5.textSize(24)  
    p5.fill(255)
    p5.textSize(20)
    p5.text("You Win!",-80,0)
    p5.pop()
    UFO.draw()
    p5.push()
    p5.imageMode(p5.CENTER)
    
    if(p5.millis() % 1000 < 500):
      p5.image(UFO.Explosion, 10, laser1.y, 50, 50)
    else:
      p5.image(UFO.Explosion, 10, laser1.y, 80, 80)

    if(p5.millis() % 1000 < 500):
      p5.image(UFO.Explosion, 290, laser2.y, 50, 50)    
    else:
      p5.image(UFO.Explosion, 290, laser2.y, 80, 80)    
    
    if(p5.millis() % 1000 < 500):
      p5.image(wave,UFO.x, UFO.y, 60, 60)
    else:
      p5.image(wave,UFO.x, UFO.y, 270, 270)    
    p5.pop()
  
  
  
  
  
  
  
  
  
  
  
  cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  p5.text(cursor_xy, 10, 20)  # cursor (x, y) 

# event function below need to be included,
# even if they don't do anything

def keyPressed(event):
  #print('keyPressed.. ' + str(p5.key))
  pass

def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  pass

def mousePressed(event):
  #print('mousePressed..')
  pass

def mouseReleased(event):
  #print('mouseReleased..')
  pass


  
