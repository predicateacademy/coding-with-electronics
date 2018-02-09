from mcpi.minecraft import Minecraft, Vec3
import mcpi.block as block
import time
import random
import words
from gpiozero import Button

mc = Minecraft.create()
x, y, z = mc.player.getPos()

def house():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-5, y-5, z-5, x+5, y+5, z+5, block.GLASS.id)
    mc.setBlocks(x-4, y-4, z-4, x+4, y+4, z+4, block.AIR.id)

def pool():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-3, y-1, z-3, x+3, y-5, z+3, block.WATER.id)

def teleport():
    x, y, z = mc.player.getPos()
    mc.player.setPos(x,y+25,z)

def draw():
    words.draw(mc, "hello hello", block.TNT.id)

def tunnel():
    # grab the players current position
    x, y, z = mc.player.getPos()

    # build an AIR tunnel down fifty blocks
    for i in range(50):
      mc.setBlock(x+1, y-i, z, block.AIR.id, 1)

    # build an AIR tunnel across (by 2) 50 blocks below ground
    for i in range(75):
      mc.setBlock(x+1+i, y-49, z, block.AIR.id, 1)
      mc.setBlock(x+1+i, y-50, z, block.AIR.id, 1)

    # build an AIR tunnel back up to the surface
    for i in range(50):
      mc.setBlock(x+1+75, y-i, z, block.AIR.id, 1)

    # create a bunker
    mc.setBlocks(x+35, y-50, z-10, x+50, y-65, z+10, block.AIR.id)

def bigbomb():
    # get players position
    x, y, z = mc.player.getPos()

    # create a big cube of TNT - how many blocks are there?
    mc.setBlocks(x-5, y-1, z-5, x+5, y-6, z+5, block.TNT.id, 1)

def sandstorm() :
   mc.postToChat("Sandstorm")
   times = 0
   while times < 100:
      x, y, z = mc.player.getPos()
      mc.setBlock(x, y+10, z, block.SAND.id)
      time.sleep(0.05)
      times = times + 1

def vacuum() :
   mc.postToChat("Vacuum")
   times = 0
   while times < 100:
      x, y, z = mc.player.getPos()
      mc.setBlocks(x-1, y-1, z-1, x+1, y+1, z+1, block.AIR.id)
      time.sleep(0.05)
      times = times + 1

def tnt() :
   mc.postToChat("TNT")
   times = 0
   while times < 100:
      x, y, z = mc.player.getPos()
      mc.setBlock(x, y, z, block.TNT.id, 1)
      time.sleep(0.05)
      times = times + 1

def teleport():
   x,y,z = mc.player.getPos()
   mc.player.setPos(x,y+25,z)

def die():
   x,y,z = mc.player.getPos()
   mc.player.setPos(x,y-3000,z)

def floor():
   x,y,z = mc.player.getPos()
   for i in range(10):
      for j in range(10):
         mc.setBlock(x+i, y, z+j, block.DIAMOND_BLOCK.id)

def cube():
   x,y,z = mc.player.getPos()
   mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.WOOD.id)
   mc.player.setPos(x,y+5,z)

def random_cube():
   length = 10
   x, y, z = mc.player.getPos()
   for i in range(length):
      for j in range(length):
         for k in range(length):
            color = random.randint(0, 15)
            mc.setBlock(x+i+1, y+j+1, z+k+1, block.WOOL.id, color)

def wall():
   x, y, z = mc.player.getPos()
   for i in range(10):
      for j in range(10):
         mc.setBlock(x, y+j, z+1+i, block.WOOD.id)

def walls():
   times = 0
   while times < 100:
      x, y, z = mc.player.getPos()
      mc.setBlocks(x, y-1, z, x, y-15, z, block.STONE.id)
      time.sleep(0.05)
      times = times + 1

def shell():
   x,y,z = mc.player.getPos()
   mc.setBlocks(x-3, y-3, z-3, x+3, y+3, z+3, block.GLASS.id)
   mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.AIR.id)

def pyramid():
   height = 10
   x, y, z = mc.player.getPos()
   level = height
   for i in range(height):
      length = (level * 2) - 1
      for j in range(length):
         for k in range(length):
            mc.setBlock(x+j+i, y+i, z+k+i, block.SAND.id)
      level -= 1

def diamond():
   height = 5
   x, y, z = mc.player.getPos()
   level = height
   for i in range(height):
       length = (level * 2) - 1
       for j in range(length):
           for k in range(length):
               mc.setBlock(x+j+i, y+height+i, z+k+i, block.DIAMOND_BLOCK.id)
               mc.setBlock(x+j+i, y+height-i, z+k+i, block.DIAMOND_BLOCK.id)
       level -= 1

def prism():
   radius = 10
   x, y, z = mc.player.getPos()
   level = radius
   for i in range(radius):
       for j in range((-1*radius), radius):
           for k in range((-1*radius), radius):
               if(abs(j)+abs(k) + i + 1 == radius):
                   mc.setBlock(x+j, y+i, z+k, block.COBBLESTONE.id)
                   mc.setBlock(x+j, y-i, z+k, block.COBBLESTONE.id)
       level -= 1

# - create our buttons
b1 = Button(5, pull_up=True)
b1.when_pressed = tunnel
