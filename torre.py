class Torre:
    def __init__(self, id):
        self._id = id;
        self._disco = []

    def sem_disco(self):
        return self._disco == []

    def empilha(self, disco):
        self._disco.insert(0, disco)

    def desempilha(self):
        self._disco.pop(0)

    def primeiro(self):
        return self._disco[0]

    def to_string(self):
        print('------------ Torre nº: ' + str(self._id) + ' ------------')
        for discos in self._disco:
            discos.to_string()
        print('')
        