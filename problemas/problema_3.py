from bio.ler_fasta import ler_fasta

def rodar_problema_3():    

    caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

    organismos_fasta = ler_fasta(caminho_do_arquivo)


    lista_nova = [] 

    for organismo in organismos_fasta:
         if organismo.sequencia[1000] == "G":
            lista_nova.append(organismo.nome)
    

    print ("Os organismos que possuem mutação no nucleotídeo de posição 1000 são: ", lista_nova)