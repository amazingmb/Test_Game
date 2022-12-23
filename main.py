import sys
import random2

class Main:
    max_width = 5
    max_height = 5
    charactwe_alive = True
    character_won = False
    monster_awake = True
    monster_awakened = False
    monster_move_per_turn = 2

    def __init__(self):
        #self.display_menu()
        pass

    def place_character(self):
        self.character_position = [0,0]

    def place_monster(self):
        self.monster_position = [random2.randint(0,self.max_height - 1), random2.randint(0,self.max_width - 1)]

    def place_trap(self):
        self.trap_position = [0,1]

    def place_flask(self):
        self.flask_position = [1,0]

    def display_menu(self):
        menu_list = ['.New Game', '.[Save Game]', '.[Load Game]', '.Options', '.Exit']
        #print('Type the number of your choice')
        print()
        for i in range (1,len(menu_list) + 1):
            print(str(i) + '' + menu_list[i - 1])
        choice = input('Select your way: ')
        self.menu_choice(choice)

    def menu_choice(self, choice):
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
        
        if(choice == 1):
            pass
        elif(choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            pass
        elif(choice == 5):
            print("Bye, my hero!")
            sys.exit(0);
        else:
            print("It`s a wrong way, try again! ")
            self.display_menu()
          
    def draw_grid(self):
        height = self.max_height
        width = self.max_width

        for y in range(0,height):
            for x in range(0,width):
                y = str(y)
                x = str(x)
                char_x = str(self.character_position[0])
                char_y = str(self.character_position[1])
                if(str(self.monster_position[0]) == x and str(self.monster_position[1]) == y and self.monster_awake == True):
                    sys.stdout.write("M")
                elif(char_x == x and char_y == y):
                    sys.stdout.write("X")
                elif(str(self.trap_position[0]) == x and str(self.trap_position[1]) == y):
                    sys.stdout.write("T")
                elif(str(self.flask_position[0]) == x and str(self.flask_position[1]) == y):
                    sys.stdout.write("F")
                else:
                    sys.stdout.write('?')
            sys.stdout.write('\r\n')

monster = Main()
monster.place_character()
monster.place_flask()
monster.place_trap()
monster.place_monster()
monster.draw_grid()