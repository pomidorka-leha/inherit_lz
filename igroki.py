import math


levels = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]



class Igrok:
    def __init__(self, name, level, opit, add_opit):
        self.name = name
        self.level = level
        self.opit = opit
        self.add_opit = add_opit

    def opit(self):
        self.opit += self.add_opit

    def show_stars(self):
        print('Имя игрока ', self.name)
        print('Уровень игрока ', self.level)
        print('Изначальный опыт игрока ', self.opit)
        print('Новый опыт игрока ', self.add_opit)
        
        self.opit += self.add_opit
        print('Текущий опыт ', self.opit)

        while self.level < len(levels) and self.opit >= levels[self.level]:
            self.level += 1
        print('Уровень повышен :) Текущий уровень ' ,self.level)
    


class Warrior(Igrok):
    def __init__(self, name, level, experience, add_exp, weapon, armor):
        super().__init__(name, level, experience, add_exp)
        self.weapon = weapon
        self.armor = armor

    def attack(self):
        while self.level < len(levels) and self.opit >= levels[self.level]:
            self.level += 1
        print('Уровень повышен :) Текущий уровень ' ,self.level)
        att = (self.level/2) * self.weapon 
        print('Атака игрока равна ', att)
        print(self.level)

    def defend(self):
        df = math.log(self.opit)*self.armor
        print('защита')
        print(df)
    def __del__(self):
        print('эт всё')



def main():
    input_data = input('Введите: Имя, Уровень, Опыт, Доп.опыт, Урон, Броня\n')
    data = input_data.split()
        
    name = data[0]
    level, exp, add_exp, weapon, armor = map(int, data[1:])
        
    player = Igrok(name, level, exp, add_exp)
    player.show_stars()
    player = Warrior(name,level,exp,add_exp,weapon,armor)
    player.attack()
    player.defend()
if __name__ == '__main__':
    main()       
