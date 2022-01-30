# This is a sample Python script.
import math
import matplotlib.pyplot as plt
import numpy as np

from datetime import date

class atom:
    def __init__(self, name , x, y, z, nr):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.id = nr

    def print(self):
    # print the atom data.
        print(f'Atom--Nr: {self.id}, Name: {self.name}, x: {self.x}, y: {self.y}, z: {self.z}')

class symm:
    def __init__(self, name, r1, r2, r3, nr):
        self.name = name
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.id = nr
    def print(self):
    # print the symmetry data.
        print(f'Symm--Nr: {self.id}, Name: {self.name}')
        print(f'      r1: {self.r1}')
        print(f'      r2: {self.r2}')
        print(f'      r3: {self.r3}')

class celldata:
    def __init__(self, name, a, b, c, alpha, beta, gamma):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def print(self):
        # print the symmetry data.
        print(f'Cell: , Name: {self.name}')
        print(f'     a: {self.a}     b: {self.b}      c: {self.c}')
        print(f' alpha: {self.alpha} beta: {self.beta} gamma: {self.gamma}')

class codeliste:
    def __init__(self, name, symm, x1, x2, x3, nr):
        self.name = name
        self.symm = symm
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.nr = nr

def dist(x1,x2,x3,y1,y2,y3):
    dsquare = (x1-y1)*(x1-y1)+(x2-y2)*(x2-y2)+(x3-y3)*(x3-y3)
    return math.sqrt(dsquare)

def draw_line(x1,y1,x2,y2,colour):
    xi = [x1,x2]
    yi = [y1,y2]
    return plt.plot(xi,yi,colour)


# Press the green button in the  gutter to run the script.
if __name__ == '__main__':
    version = '1.0.1'
    Author = 'EF'
    today = date.today()
    print(f'Edi_Kplot: Author:{Author} Version:{version} Datum:{today}')
    print('')
    print('------Celldata--------')
    cellA = celldata('Zyklin', 1.0, 2.0, 3.0, 90., 84.3, 90.)
    cellA.print()
    print('------Atoms--------')
    atoms = {
        atom('mg1', 0.42, 0.28, 0.37, 1),
        atom('o1', 0.72, 0.02, 0.39, 2),
        atom('o2', 0.22, 0.27, 0.54, 3)
    }
    for myatom in atoms:
        myatom.print()
    print('------Symmetries--------')
    symms = {
        # Space Group P21/c
        #'x, y, z'
        symm('E', [1,0,0,0], [0,1,0,0], [0,0,1,0], 1),
        #'-x, 1/2+y, 1/2-z'
        symm('21', [-1,0,0,0], [0,1,0,0.5], [0,0,-1,0.5], 2),
        # '-x, -y, -z'
        symm('i', [-1,0,0,0], [0,-1,0,0], [0,0,-1,0], 3),
        # 'x, 1/2-y, 1/2+z'
        symm('c', [1,0,0,0], [0,-1,0,0.5], [0,0,1,0.5], 4)
    }

    for mysymm in symms:
        mysymm.print()
    print('------all atoms in Cell--------')
    icodes = 0
    cellbuffer = []

    #---loop1 over atoms
    for myatom in atoms:
   #---loop2 over symms
        for mysymm in symms:
            # cell coordinates
            x1 = mysymm.r1[0]*myatom.x+mysymm.r1[1]*myatom.y+mysymm.r1[2]*myatom.z+mysymm.r1[3]
            x2 = mysymm.r2[0]*myatom.x+mysymm.r2[1]*myatom.y+mysymm.r2[2]*myatom.z+mysymm.r2[3]
            x3 = mysymm.r3[0]*myatom.x+mysymm.r3[1]*myatom.y+mysymm.r3[2]*myatom.z+mysymm.r3[3]
            print(f'Atom: {myatom.name}, Symm: {mysymm.name}: X {x1:9.4f}, Y {x2:9.4f}, Z {x3:9.4f}')
            # orthogonal coordinates
            xorth1 = cellA.a * x1
            xorth2 = cellA.b * x2
            xorth3 = cellA.c * x3
            print(f' X.: {xorth1:9.4f}, Y.: {xorth2:9.4f}, Z.: {xorth3:9.4f}')
            #---------------------------------------------------------------
            #save atoms in cellbuffer
            cellbuffer.append(codeliste(myatom.name,mysymm.name,xorth1,xorth2,xorth3,icodes))
            icodes += 1
            #
    print(f'total atoms in cell: {icodes}')
    print('------distances--------')
    c_nr = 0
    #loop 1st code
    for code1 in cellbuffer:
        for code2 in cellbuffer:
            if(code1.nr < code2.nr):
                c_nr += 1
                d = dist(code1.x1,code1.x2,code1.x3,code2.x1,code2.x2,code2.x3)
                print(f'{c_nr}: {code1.name} {code1.symm} {code2.name} {code2.symm} : {d:5.2f}')
    #loop 2nd code
    print(f'{c_nr} distances processed')

    #------------------------------------
    #orientation
    # rotation matrix
    #
    #  axis: c
    #  (0.5   -0.667    0)
    #  (0.667  0.5      0)
    #  (0      0        1)
    rotx = [0.500,-0.667, 0.]
    roty = [0.667, 0.5,   0.]
    rotz = [0.,    0.,    1.]



    #--------------------------------------
    print('')
    print('---------------------------------------')
    figure, axes = plt.subplots()
    # evenly sampled time at 200ms intervals
    #tc = np.arange(0., cellA.c, 0.2)
    #tb = np.arange(0., cellA.b, 0.2)

    # red dashes, blue squares and green triangles
    draw_line(0., 0., 0., cellA.c, 'r--')  # 0 0 0 - 0 0 1
    draw_line(0., 0., cellA.b, 0., 'r--')  # 0 0 0 - 0 1 0
    draw_line(0., cellA.c, cellA.b, cellA.c, 'r--')  # 0 0 1 - 0 1 1
    draw_line(cellA.b, cellA.c, cellA.b, 0., 'r--')  # 0 1 1 - 0 1 0

    #draw_line(0.,0.,1.,1.,'y:')

    plt.axis([-1., cellA.b+1., -1., cellA.c+1.])
    for code0 in cellbuffer:
        if code0.name == 'mg1':
            Drawing_colored_circle = plt.Circle((code0.x2, code0.x3), 0.08, color='g')
        else:
            Drawing_colored_circle = plt.Circle((code0.x2, code0.x3), 0.05, color='b')
        axes.add_artist(Drawing_colored_circle)
        #print(f'plotted: {code0.nr}')

    plt.title(cellA.name)
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
