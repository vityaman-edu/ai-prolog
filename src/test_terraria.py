from typing import Iterable, Set
import unittest
from unittest import TestCase

from args import Args
from log import Log
from prolog import Prolog
from terraria import Terraria, TerrariaException
from dsl import *


def reprset(iterable: Iterable[object]) -> Set[str]:
    return {repr(element) for element in iterable}


class TerrariaTest(TestCase):
    def test(self):
        Log.set_level(Log.Level.Debug)
        args = Args(knowledge_path='res')
        with Prolog(args.preload) as prolog:
            terraria = Terraria(prolog)

            # Initially empty
            self.assertEqual(reprset(terraria.inventory()), set())
            self.assertEqual(reprset(terraria.places()), set())

            # Explore
            terraria.explore(Ore.Iron)
            terraria.explore(Ore.Gold)

            self.assertEqual(reprset(terraria.inventory()), set())
            self.assertEqual(reprset(terraria.places()), {
                repr(Ore.Iron),
                repr(Ore.Gold),
            })

            # Explore Evil
            terraria.explore(EvilBiome.Corruption)

            self.assertEqual(reprset(terraria.inventory()), set())
            self.assertEqual(reprset(terraria.places()), {
                repr(Ore.Iron),
                repr(Ore.Gold),
                repr(EvilBiome.Corruption)
            })

            # Pick a pickaxe
            terraria.cheat(Pickaxe.Copper)

            self.assertEqual(reprset(terraria.inventory()), {
                repr(Pickaxe.Copper),
            })
            self.assertEqual(reprset(terraria.places()), {
                repr(Ore.Iron),
                repr(Ore.Gold),
                repr(EvilBiome.Corruption)
            })

            # Take
            terraria.take(Ore.Iron)
            terraria.take(Pickaxe.Iron)

            self.assertEqual(reprset(terraria.inventory()), {
                repr(Pickaxe.Copper),
                repr(Pickaxe.Iron),
                repr(Ore.Iron),
            })
            self.assertEqual(reprset(terraria.places()), {
                repr(Ore.Iron),
                repr(Ore.Gold),
                repr(EvilBiome.Corruption)
            })

            # Take failure
            self.assertRaises(
                TerrariaException,
                lambda: terraria.take(Ore.Gold))

            # Available
            terraria.explore(Ore.Copper)
            terraria.explore(Ore.Iron)
            terraria.explore(Ore.Gold)
            terraria.explore(Ore.Silver)

            self.assertEqual(reprset(terraria.available()), {
                repr(Ore.Silver),
                repr(Ore.Copper),
            })

            terraria.take(Ore.Silver)

            self.assertEqual(reprset(terraria.available()), {
                repr(Pickaxe.Silver),
                repr(Ore.Copper),
            })


if __name__ == '__main__':
    unittest.main()
