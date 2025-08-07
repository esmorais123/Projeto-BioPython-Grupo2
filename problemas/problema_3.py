from bio.ler_fasta import ler_fasta

def rodar_problema_3():    

    caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

    organismos_fasta = ler_fasta(caminho_do_arquivo)

    lista_com_mutacao = []
    lista_sem_mutacao = []

    for organismo in organismos_fasta:
        if organismo.sequencia[999] == "G":
            lista_com_mutacao.append(organismo.nome)
        else:
            lista_sem_mutacao.append(organismo.nome)
    
    print("Os organismos que possuem mutação no nucleotídeo de posição 1000 são: ", lista_com_mutacao)
    print("Os organismos que NÃO possuem mutação no nucleotídeo de posição 1000 são: ", lista_sem_mutacao)
