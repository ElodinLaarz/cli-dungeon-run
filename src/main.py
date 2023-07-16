import runner.dungeon_runner as dungeon_runner

def main():
    print("Welcome! Get ready for Grand adventures in the game that awaits you!")
    print("Choose a Name for yourself!")
    name = input()
    dungeon = dungeon_runner.DungeonRun(name)
    dungeon.Start()

if __name__ == "__main__":
    main()
