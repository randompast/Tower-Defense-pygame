from init import initialize
from gameloop import gameloop

def main():
    pyg = initialize()
    gameloop(pyg)

if __name__ == '__main__':
    main()