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
    
    def complementar(self):
        conversor_de_bases = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
        sequencia_complementar = ""
        for base in self.sequencia:
            sequencia_complementar = sequencia_complementar + conversor_de_bases[base]
        return Sequencia(sequencia_complementar)
    
    def complementar_reversa(self):
        sequencia_complementar = self.complementar()
        sequencia_reversa = sequencia_complementar.sequencia[::-1]
        return Sequencia(sequencia_reversa)

    def transcrever(self):
        conversor_de_bases = {
            'A': 'U',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
        sequencia_rna = ""
        for base in self.sequencia:
            sequencia_rna = sequencia_rna + conversor_de_bases[base]
        return Sequencia(sequencia_rna)