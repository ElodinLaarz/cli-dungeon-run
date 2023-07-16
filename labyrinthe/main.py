import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import dungeon_runner as dungeon_runner

def main():
    print("Welcome! Get ready for Grand adventures in the game that awaits you!")
    print("Choose a Name for yourself!")
    name = input()
    dungeon = dungeon_runner.DungeonRun(name)
    dungeon.Start()

if __name__ == "__main__":
    main()
