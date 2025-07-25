from bio.ler_fasta import ler_fasta

def rodar_problema_2():

    caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

    organismos_fasta = ler_fasta(caminho_do_arquivo)

    for organismo in organismos_fasta:
        #print("Sequência original:", organismo.sequencia)
        print(f"A proteína traduzida para o organismo {organismo.nome.split(',')[0]} é {organismo.sequencia.traduzir(parar=False)}\n")