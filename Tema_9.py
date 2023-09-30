from datetime import datetime
print(datetime.now())  # Выводит текущую дату и время

class Tomato:
    states = {
        0: 'отсутствует',
        1: 'цветение',
        2: 'зеленый',
        3: 'красный'
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Помидоры проходят следующие стадии созревания:")
        for state_num, state_name in Tomato.states.items():
            print(f"   {state_num}: {state_name}")
        print("2. Садовник может работать, ухаживая за растением и собирая урожай.")
        print("3. Чтобы собрать урожай, все помидоры должны быть спелыми.")

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрала урожай!")
            self._plant.give_away_all()
        else:
            print("Помидоры еще не дозрели. Подождите еще немного.")


# Тесты
if __name__ == "__main__":
    Gardener.knowledge_base()  # тест 1: справка по садоводству

    tomato_bush = TomatoBush(5)  # тест 2: создание объектов классов TomatoBush и Gardener
    gardener = Gardener("Полина", tomato_bush)

    for _ in range(3):  # тест 3: ухаживаем за растением несколько раз
        gardener.work()

    gardener.harvest()  # тест 4: попытка собрать урожай до созревания

    for _ in range(2):  # продолжаем ухаживать за растением
        gardener.work()

    gardener.harvest()  # тест 5: сбор урожая после созревания