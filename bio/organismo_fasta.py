from bio.sequencia import Sequencia

class OrganismoFasta:

    def __init__(self, id, nome, sequencia):
        self.id = id
        self.nome = nome
        self.sequencia = Sequencia(sequencia) #Cria um novo objeto da classe Sequencia.
