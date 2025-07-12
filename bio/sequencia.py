class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)

    def calcular_tamanho(self):
        return len(self.sequencia)
    
    def percentual(self, bases):
        tamanho = self.calcular_tamanho()
        count = 0
        for base_especifica in self.sequencia:
            if base_especifica in bases:
                count = count + 1 
        
        percentual = count / tamanho
        return percentual 

      