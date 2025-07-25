from bio.sequencia import Sequencia
from bio.constantes import DNA_PARA_AMINOACIDO

class OrganismoFasta:

    def __init__(self, id, nome, sequencia):
        self.id = id
        self.nome = nome
        self.sequencia = Sequencia(sequencia)
