class Critter:
    total = 0

    @staticmethod
    def status():
        print('Общее число зверюшек', Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def talk(self):
        print("Меня зовут",self.name )  

    def __str__(self):
        ans = 'Объект класа Critter\n'
        ans += 'имя:'+ self.name +'\n' 
        return ans 

def main():
    print('Доступ к атрибуту класа Critter.total:', end="")
    print(Critter.total)

    print("Создание зверюшек.")
    crit1 = Critter('Зверюшка 1')
    crit2 = Critter('Зверюшка 2')
    crit3 = Critter('Зверюшка 3')

    Critter.status()

    print("Доступ к атрибуту класа через объект:", end=" ")
    print(crit1.total)

main()