from startcode.tictactoe.mytictactoe import initialiseer_bord, print_bord, zet, controleer_winnaar


def tic_tac_toe():
    bord = initialiseer_bord()
    huidige_speler = 'x'
    einde_spel = False
    winnaar = ""
    teller = 0
    while not einde_spel:
        print_bord(bord)
        rij = int(input("Doe een zet."))
        kolom = int(input("Doe een zet in een kolom."))

        bord = zet(bord, rij, kolom, huidige_speler)
        if (controleer_winnaar(bord)== True):
            print(f"huidige_speler) heeft gewonnen!")

        if huidige_speler == 'x':
           huidige_speler = 'o'
        else:
            huidige_speler = 'x'

tic_tac_toe()