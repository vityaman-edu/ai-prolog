from log import Log
from prolog import Prolog
from args import Args
from dsl import *
from terraria import Terraria
import os

if __name__ == '__main__':
    Log.set_level(Log.Level.Debug)
    args = Args.system()
    with Prolog(args.preload) as prolog:
        terraria = Terraria(prolog)
        terraria.explore(Ore.Gold)
        print(list(terraria.inventory()))
        print(list(terraria.places()))
