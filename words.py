import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import subprocess
import copy

def build_A(mc, blkid, pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, blkid,1)
	mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y +4,pos.z, blkid,1)
	mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+1,pos.y +4,pos.z, blkid,1)
	mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y +2,pos.z, blkid,1)

def build_B(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y +1,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y +2,pos.z, blkid,1)

def build_C(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y +4,pos.z, blkid,1)

def build_D(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +2,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y +2,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y +4,pos.z, blkid,1)

def build_E(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y +2,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y ,pos.z, blkid,1)

def build_F(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y +2,pos.z, blkid,1)

def build_G(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +3,pos.z, blkid,1)          
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+1 ,pos.z, blkid,1)

def build_H(mc, blkid, pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, blkid,1)
	mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y +2,pos.z, blkid,1)
	mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y +4,pos.z, blkid,1)

def build_I(mc, blkid, pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y,pos.z, blkid,1)
	mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y +4,pos.z, blkid,1)
	mc.setBlocks(pos.x+1 , pos.y+1 , pos.z, pos.x+1,pos.y +3,pos.z, blkid,1)

def build_J(mc, blkid, pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y,pos.z, blkid,1)
	mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y +4,pos.z, blkid,1)
	mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y +3,pos.z, blkid,1)

def build_K(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+1,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+4 ,pos.z, blkid,1)


def build_L(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, blkid,1)


def build_M(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +3,pos.z, blkid,1)          
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+3,pos.z, blkid,1)
        mc.setBlocks(pos.x+4 , pos.y , pos.z, pos.x+4,pos.y+3,pos.z, blkid,1)
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+4,pos.y+4 ,pos.z, blkid,1)

def build_N(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +3,pos.z, blkid,1)          
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+3,pos.z, blkid,1)

def build_O(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+1,pos.y+4 ,pos.z, blkid,1)

def build_P(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y+2,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+3 ,pos.z, blkid,1)

def build_Q(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y+2 , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+1,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+4 ,pos.z, blkid,1)
        mc.setBlocks(pos.x+3 , pos.y , pos.z, pos.x+2,pos.y ,pos.z, blkid,1)

def build_R(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x,pos.y+2,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+3,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+1 ,pos.z, blkid,1)

def build_S(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y,pos.z, blkid,1)          
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+2,pos.z, blkid,1)          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2,pos.z, blkid,1)
        mc.setBlocks(pos.x , pos.y+2 , pos.z, pos.x,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)

def build_T(mc, blkid, pos):
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y+3,pos.z, blkid,1)          
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)          

def build_U(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y,pos.z, blkid,1)          
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)          

def build_V(mc, blkid, pos):
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y,pos.z, blkid,1)          
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+4,pos.z, blkid,1)          
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)          

def build_W(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+4,pos.y,pos.z, blkid,1)          
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+4,pos.z, blkid,1)
        mc.setBlocks(pos.x+4 , pos.y+1 , pos.z, pos.x+4,pos.y+4 ,pos.z, blkid,1)

def build_X(mc, blkid, pos):
        mc.setBlock(pos.x+1 , pos.y+2 , pos.z, blkid,1)
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+1 ,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+1 ,pos.z, blkid,1)
        mc.setBlocks(pos.x , pos.y+3 , pos.z, pos.x,pos.y+4 ,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+4 ,pos.z, blkid,1)

def build_Y(mc, blkid, pos):
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y+3 ,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+4 ,pos.z, blkid,1)
        mc.setBlocks(pos.x , pos.y+3 , pos.z, pos.x,pos.y+4 ,pos.z, blkid,1)

def build_Z(mc, blkid, pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y ,pos.z, blkid,1)
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+2 ,pos.z, blkid,1)
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2 ,pos.z, blkid,1)
        mc.setBlocks(pos.x+2 , pos.y+2 , pos.z, pos.x+2,pos.y+4 ,pos.z, blkid,1)
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+1,pos.y+4 ,pos.z, blkid,1)

def draw(mc, txt, blkid):
        find_centre = len(txt) *2

        player_pos = mc.player.getPos()
        start_pos = copy.copy(player_pos)
        mc.camera.setPos(player_pos.x +find_centre, player_pos.y, player_pos.z + 15)

        for letter in txt:
                if letter == 'A' or letter == 'a':
                        build_A(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'B' or letter == 'b':
                        build_B(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'C' or letter == 'c':
                        build_C(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'D' or letter == 'd':
                        build_D(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'E' or letter == 'e':
                        build_E(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'F' or letter == 'f':
                        build_F(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'G' or letter == 'g':
                        build_G(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'H' or letter == 'h':
                        build_H(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'I' or letter == 'i':
                        build_I(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'J' or letter == 'j':
                        build_J(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'K' or letter == 'k':
                        build_K(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'L' or letter == 'l':
                        build_L(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'M' or letter == 'm':
                        build_M(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+6
                elif letter == 'N' or letter == 'n':
                        build_N(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'O' or letter == 'o':
                        build_O(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'P' or letter == 'p':
                        build_P(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'Q' or letter == 'q':
                        build_Q(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+5
                elif letter == 'R' or letter == 'r':
                        build_R(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'S' or letter == 's':
                        build_S(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'T' or letter == 't':
                        build_T(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'U' or letter == 'u':
                        build_U(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'V' or letter == 'v':
                        build_V(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'W' or letter == 'w':
                        build_W(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+6
                elif letter == 'X' or letter == 'x':
                        build_X(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == 'Y' or letter == 'y':
                        build_Y(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+6
                elif letter == 'Z' or letter == 'z':
                        build_Z(mc, blkid, player_pos)
                        player_pos.x = player_pos.x+4
                elif letter == ' ': 
                        player_pos.x = player_pos.x+4
                else:
                        print "sorry that word uses letters we don't know how to build"        

