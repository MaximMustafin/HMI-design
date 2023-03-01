import pygame as pg

pg.init()

FONTS = [pg.font.SysFont("freemono", 80), pg.font.SysFont("arial", 80), pg.font.SysFont("imperialscript", 80),
         pg.font.SysFont("alumnisanscollegiateone", 80), pg.font.SysFont("ambidexter", 80), pg.font.SysFont("blakahollow", 80),
         pg.font.SysFont("gochihand", 80), pg.font.SysFont("himelody", 80), pg.font.SysFont("moolahlah", 80), 
         pg.font.SysFont("rubikbubbles", 80)]

PICTOGRAMS = {
        "1":[[0, 0, 0],     # 1
         [0, 1, 0],
         [0, 0, 0]],

        "2":[[0, 0, 0],     # 2
         [1, 1, 0],
         [0, 0, 0]],

        "3":[[0, 1, 0],     # 3
         [1, 0, 1],
         [0, 0 ,0]],

        "4":[[1, 1, 1],     # 4
         [0 ,1, 0],
         [0, 0, 0]],

        "5":[[1, 0, 1],     # 5
         [0, 1, 0],
         [1, 0, 1]],

        "6":[[1, 1, 1],     # 6
         [1, 1, 1],
         [0, 0 ,0]],

        "7":[[1, 1, 1],     # 7
         [1, 1, 1,],
         [0, 1, 0]],

        "8":[[1, 0, 1],     # 8
         [1, 1, 1],
         [1, 1, 1]],

        "9":[[1, 1, 1],     # 9
         [1, 1, 1],
         [1, 1, 1]],
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'