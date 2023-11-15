class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.bird.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fish)}"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.bird)}"

        result += f"\nTotal animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())

for animal_info in range(number_of_animals):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))