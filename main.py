import dungeon_runner as dr

def main():
    print("Welcome! Get ready for Grand adventures in the game that awaits you!")
    print("Choose a Name for yourself!")
    name = input()
    dungeon = dr.DungeonRun(name)
    dungeon.Start()
    
if __name__ == "__main__":
    main()