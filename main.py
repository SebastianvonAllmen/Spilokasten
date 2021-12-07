from classes.emblem import emblem
from classes.row import row

def main():
    melone = emblem("m", 20, 0.1)
    citrone = emblem("c", 20, 0.1)
    kirsche = emblem("k", 20, 0.1)
    traube = emblem("t", 20, 0.1)
    orange = emblem("O", 20, 0.1)
    bar = emblem("BAR", 20, 0.1)
    seven = emblem("7", 20, 0.1)
    Bonus = emblem("BBB", 20, 0.1)
    glocke = emblem("G", 20, 0.1)
    dia = emblem("D", 20, 0.1)

    crtrow = row(melone, orange, dia)


    print(melone.character)





    








if __name__ == "__main__":
    main()