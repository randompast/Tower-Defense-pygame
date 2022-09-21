import pygame

class grid():
    def __init__(self, dims, size, offset_lr, offset_tb):
        self.dims = dims
        self.size = size
        self.offset_lr = offset_lr
        self.offset_tb = offset_tb
        self.setgrid()
        self.res = self.get_size()
        print(self.res)

    def setgrid(self):
        self.grid = [ [0]*(self.dims[0]) for i in range(self.dims[1]) ]
        # self.grid[3] = [None,None,None,0,0,0,0,0]
        # self.grid = [ [0]*8
        #                 ,[1]*7 + [0]
        #                 ,[0]*8
        #                 ,[0]+ [1]*7
        #                 ,[0]*8
        #                 ,[1]*7 + [0]
        #                 ,[0]*8
        #                 ,[0]+ [1]*7
        #              ]

    def get_size(self):
        w = self.dims[0] * self.size[0] + sum(self.offset_lr)
        h = self.dims[1] * self.size[1] + sum(self.offset_tb)
        return [w,h]

    def print(self):
        print()
        for row in self.grid:
            print([i for i in row])

    def draw_grid(self, pyg):
        for r in range(0, self.dims[0]):
            for c in range(0, self.dims[1]):
                if self.grid[r][c]:
                    self.draw_circ(pyg, [c,r], [0.5,0.5], 0.3, (0,0,100))

    def draw_grid_lines(self, pyg):
        for x in range(0, self.dims[0]+1):
            px = self.offset_lr[0] + x*self.size[0]
            top = self.offset_tb[0]
            bot = self.res[1] - self.offset_tb[1]
            spos = [px, top]
            epos = [px, bot]
            pygame.draw.line(pyg.DISPLAYSURF, pyg.BLACK, spos, epos)
        for y in range(0, self.dims[1]+1):
            py = self.offset_tb[0] + y*self.size[0]
            l = self.offset_lr[0]
            r = self.res[0] - self.offset_lr[1]
            spos = [l, py]
            epos = [r, py]
            pygame.draw.line(pyg.DISPLAYSURF, pyg.BLACK, spos, epos)

    def mouse_to_grid(self, xy):
        x = xy[0] - self.offset_lr[0]
        y = xy[1] - self.offset_tb[0]
        gx = x//self.size[0]
        gy = y//self.size[1]
        return gx,gy

    def grid_to_xy(self, g, off):
        x = (g[0]+off[0])*self.size[0] + self.offset_lr[0]
        y = (g[1]+off[1])*self.size[1] + self.offset_tb[0]
        return x,y

    def draw_circ(self, pyg, pos, off, size, color):
        xy = self.grid_to_xy(pos, off)
        pygame.draw.circle(pyg.DISPLAYSURF, color, xy, min(self.size)*size*0.5)

    def inbounds(self, gpos):
        return 0 <= gpos[0] < self.dims[0] and 0 <= gpos[1] < self.dims[1]