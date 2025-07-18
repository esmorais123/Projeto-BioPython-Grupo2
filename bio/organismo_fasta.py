from bio.sequencia import Sequencia
from bio.constantes import DNA_PARA_AMINOACIDO

class OrganismoFasta:

    def __init__(self, id, nome, sequencia):
        self.id = id
        self.nome = nome
        self.sequencia = Sequencia(sequencia)

    def traduzir(self, parar=False):
        proteina = ""

        for i in range(0, len(self.sequencia) - 2, 3):
            codon = self.sequencia[i:i+3]
            aminoacido = DNA_PARA_AMINOACIDO.get(codon, "X")  
            if parar and aminoacido == "*":
                break

            proteina += aminoacido

        return proteina