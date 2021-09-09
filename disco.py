class Disco:
    def __init__(self, peso):
        self._peso = peso

    def peso_disco(self):
        return self._peso

    def to_string(self):
        for _ in range(self._peso):
            print('-', end='')
            
        print(' ' + str(self._peso))