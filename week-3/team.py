import akos
import ati
import demo2
import marianna


def main_menu():
    choose = input('\n****************************************\n                                      \n Please choose: \n\n****************************************\n\n 2 - Csordas Attila\n\n 3 - Maurer-Somogyi Akos \n\n 4 - Tombacz Kristof\n\n Q - quit the menu \n\n****************************************\n  Type the number or quit: ').lower()
    while choose != 'q':
        if choose == '1':
            marianna.search_palindromes('dog goat dad duck doodle never')
        if choose == '2':
            ati.user_input()
        elif choose == '3':
            akos.menu()
        elif choose == '4':
            demo2.main()
        choose = input('\n****************************************\n                                      \n Please choose: \n\n****************************************\n\n 2 - Csordas Attila\n\n 3 - Maurer-Somogyi Akos \n\n 4 - Tombacz Kristof\n\n Q - quit the menu \n\n****************************************\n  Type the number or quit: ').lower()

main_menu()
