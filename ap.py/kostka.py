import random

def hod_kostkou():

    obrazky_kostek = {

    1: (

        "┌─────────┐",
        "│    1    │",
        "│    ●    │",
        "│         │",
        "└─────────┘",

    ),

    2: (

        "┌─────────┐",
        "│  ●      │",
        "│    2    │",
        "│      ●  │",
        "└─────────┘",

    ),

    3: (

        "┌─────────┐",
        "│  ● 3    │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",

    ),

    4: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│    4    │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    5: (

        "┌─────────┐",
        "│  ● 5 ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ● 6 ●  │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

}

    hod = input("ano, nebo ne: ")

    while hod.lower() == "Ano".lower():
        kostka1 = random.randint(1,6)
        kostka2 = random.randint(1,6)
        
        print("padlo ti: {} a {}". format(kostka1, kostka2))
        print("\n".join(obrazky_kostek[kostka1]))
        print("\n".join(obrazky_kostek[kostka2]))
        break

    else:
        print("Neházím kostkou.")

hod_kostkou()
