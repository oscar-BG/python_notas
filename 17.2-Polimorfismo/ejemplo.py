class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau guau!"
    
class Gato(Animal):
    def hablar(self):
        return "Miau miau"
    

def hacer_hablar(animal):
    print(animal.hablar())

perro = Perro()
gato = Gato()

hacer_hablar(perro)
hacer_hablar(gato)