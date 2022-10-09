import os
import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

minuteAngle=0
hourAngle=180

VertexList = [[(-0.500000+0.9),0.123431-0.2,0.000000],
[-0.443431+0.9,0.500000-0.2,0.000000],
[-0.556569+0.9,0.500000-0.2,0.000000],
[-0.500000+0.9,0.556569-0.2,0.000000],
[0.400000,0.250503,0.000000],
[0.949497,0.300000,0.000000],
[0.350502,0.300000,0.000000],
[0.400000,0.349498,0.000000]]

# 2 triangles (hr)
hourHandIndex=[[1,2,0],[1,3,2]]

# 2 triangles (min)
minuteHandIndex=[[5,7,6],[4,6,5]]

def drawcircle():
    glColor3f(1,1,0)
    glPointSize(5.0)
    a = 0.0
    r = 0.0
    while r<0.55:
        a=0.0
        while a<2*math.pi:
            x = r*math.sin(a)
            y = r*math.cos(a)
            glBegin(GL_POINTS)
            glVertex2f(x+0.4,y+0.3)
            glEnd()
            a += 0.01
        r += 0.01

def drawhourHand():
    glColor3f(1,0,0)
    glTranslate(0.4,0.3,0)
    glRotate(-hourAngle,0,0,1);
    glTranslate(-0.4,-0.3,0)
    glBegin(GL_TRIANGLES) 
    for fID in hourHandIndex:
        glVertex3fv(VertexList[fID[0]])
        glVertex3fv(VertexList[fID[1]])
        glVertex3fv(VertexList[fID[2]])
    glEnd()


def drawminuteHand():
    glColor3f(0,2,0)
    glTranslate(0.4,0.3,0)
    glRotate(-minuteAngle,0,0,1);
    glTranslate(-0.4,-0.3,0)
    glBegin(GL_TRIANGLES) 
    for fID in minuteHandIndex:
        glVertex3fv(VertexList[fID[0]])
        glVertex3fv(VertexList[fID[1]])
        glVertex3fv(VertexList[fID[2]])
    glEnd()



def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix() 
    drawcircle()
    
    # draw hour
    glPushMatrix() 
    drawhourHand()
    glPopMatrix()
    # draw minute
    drawminuteHand()
    
    
    glPopMatrix()
    glutSwapBuffers()

def move(n):
    global hourAngle
    global minuteAngle
    hourAngle=hourAngle+1
    minuteAngle=minuteAngle+12
    glutPostRedisplay()
    glutTimerFunc(10, move, 0)

def reshape(width,height):
    glViewport(0, 0, width, height)

def keyboard( key, x, y ):
    if key == b'\x1b': #ESC
        os._exit(0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutCreateWindow(b'Homework2')
glutReshapeWindow(800,800)
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutTimerFunc(10, move, 0);
glutKeyboardFunc(keyboard)
glutMainLoop()
