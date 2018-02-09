import mcpi.minecraft as minc
import mcpi.block as block
import random, time, pygame
pygame.mixer.init()
earthSound = pygame.mixer.Sound('earthquake.ogg')
eruptSound = pygame.mixer.Sound('lava.ogg')
meteorSound = pygame.mixer.Sound('meteor.ogg')

def earthquake(mc, x, z):
    mc.postToChat('Earthquake!')
    y = mc.getHeight(x, z)
    endtime = time.time() + 60
    nearthtime = time.time()
    while endtime > time.time():
        if time.time() > nearthtime:
            earthSound.play()
            nearthtime = time.time() + 5
        ppos = mc.player.getPos()
        if ppos.x < x+15 and ppos.x > x-15:
            if ppos.y < y+15 and ppos.y > -60:
                if ppos.z < z+15 and ppos.z > z-15:
                    mc.player.setPos(ppos.x, ppos.y, ppos.z)
        bx = random.randint(x-15, x+15)
        by = y
        bz = random.randint(z-15, z+15)
        if mc.getHeight(bx, bz) > -50:
            by = mc.getHeight(bx, bz)
        if mc.getBlock(bx, by, bz) in [block.GLASS.id, block.GLASS_PANE.id]:
            mc.setBlock(bx, by, bz, block.AIR.id)
            continue
        mc.setBlock(bx, by, bz, block.GRAVEL.id)
        mc.setBlocks(bx, by-1, bz, bx, -60, bz, block.AIR.id)

def sinkhole(mc, x, z):
    blks = []
    y = mc.getHeight(x, z)
    xdist = random.randint(1, 5)
    for bx in range(-xdist, xdist+1):
        zdist = random.randint(1, 5)
        for bz in range(-zdist, zdist+1):
            blks.append([x+bx, z+bz])
    earthSound.play()
    for blk in blks:
        mc.setBlocks(blk[0], mc.getHeight(blk[0], blk[1]), blk[1], blk[0], -60, blk[1], block.AIR.id)
        mc.setBlocks(blk[0], -55, blk[1], blk[0], -60, blk[1], block.LAVA.id)
    for blk in blks:
        mc.setBlock(blk[0], y, blk[1], block.GRAVEL.id)

def geyser(mc, x, z):
    y = mc.getHeight(x, z)
    mc.setBlocks(x-2, y+5, z-2, x+2, -60, z+2, block.WATER.id)
    time.sleep(25)
    mc.setBlocks(x-2, y+5, z-2, x+2, -60, z+2, block.AIR.id)

def eruption(mc, x, z):
    y = mc.getHeight(x, z)
    for i in range(3):
        eruptSound.play()
        mc.setBlocks(x-2, y+9, z-2, x+2, y+9, z+2, block.LAVA.id)
        eruptSound.play()
        for i in range(15):
            time.sleep(1)
            eruptSound.play()
        eruptSound.play()
        mc.setBlocks(x-2, y+10, z-2, x+2, y+10, z+2, block.WATER.id)
        eruptSound.play()
        for i in range(5):
            time.sleep(1)
            eruptSound.play()
        eruptSound.play()
        mc.setBlocks(x-2, y+10, z-2, x+2, y+10, z+2, block.AIR.id)
        eruptSound.play()
        for i in range(5):
            time.sleep(1)
            eruptSound.play()
        eruptSound.play()
        y += 1
        eruptSound.play()

def meteor(mc, x, z):
    mc.postToChat('Meteor approaching!')
    y = 64
    h = mc.getHeight(x, z)
    x -= (64 - h)
    meteorSound.play()
    while y > h:
        y -= 1
        x += 1
        mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.OBSIDIAN.id)
        time.sleep(0.05)
        mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.AIR.id)
    mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.LAVA.id)
    mc.setBlocks(x-1, y-1, z-1, x+1, y+1, z+1, block.OBSIDIAN.id)

def meteor_shower(mc, x, z):
    for i in range(10):
        mx = random.randint(x-15, x+15)
        mz = random.randint(z-15, z+15)
        meteor(mc, mx, mz)

def heatwave(mc, x, z):
    y = mc.getHeight(x, z)
    endtime = time.time() + random.randint(50, 90)
    while time.time() < endtime:
        blkid = block.AIR.id
        while blkid == block.AIR.id:
            bx = random.randint(x-10, x+10)
            by = random.randint(y, y+10)
            bz = random.randint(z-10, z+10)
            blkid = mc.getBlockWithData(bx, by, bz).id
        blk = blkid
        blkd = mc.getBlockWithData(bx, by, bz).data
        if blkid == block.GRASS.id:
            blk = block.DIRT.id
            blkd = 0
        elif blkid in [block.WATER.id, block.WATER_FLOWING.id, block.WATER_STATIONARY.id]:
            blk = block.WATER.id
            blkd = 1
        elif blkid == block.LEAVES.id:
            blk = block.COBWEB.id
            blkd = 0
        elif blkid == block.WOOD.id:
            blk = block.LAVA_STATIONARY.id
            blkd = 1
        mc.setBlock(bx, by, bz, blk, blkd)

def tsunami(mc, x, z):
    tend = time.time() + 15
    tx = x
    while time.time() < tend:
        h = mc.getHeight(tx, z)
        mc.setBlocks(tx, h-5, z-5, tx, h+5, z+5, block.WATER_STATIONARY.id)
        time.sleep(0.1)
        mc.setBlocks(tx, h-5, z-5, tx, h+5, z+5, block.AIR.id)
        time.sleep(0.1)
        tx += 1
    hm = 5
    while hm > -1:
        h = mc.getHeight(tx, z)
        mc.setBlocks(tx, h-int(hm), z-5, tx, h+int(hm), z+5, block.WATER_STATIONARY.id)
        time.sleep(0.1)
        mc.setBlocks(tx, h-int(hm), z-5, tx, h+int(hm), z+5, block.AIR.id)
        time.sleep(0.1)
        tx += 1
        hm -= 0.2

