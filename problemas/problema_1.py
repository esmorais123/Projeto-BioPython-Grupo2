from bio.ler_fasta import ler_fasta

def rodar_problema_1():
    
    caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

    organismos_fasta = ler_fasta(caminho_do_arquivo)

    for organismo in organismos_fasta:
        print(f"O percentual de A do organismo {organismo.nome} é {organismo.sequencia.percentual('A'):.2f} %")
        print(f"O percentual de T do organismo {organismo.nome} é {organismo.sequencia.percentual('T'):.2f} %")
        print(f"O percentual de C do organismo {organismo.nome} é {organismo.sequencia.percentual('C'):.2f} %")
        print(f"O percentual de G do organismo {organismo.nome} é {organismo.sequencia.percentual('G'):.2f} %")
        print(f"O percentual de GC do organismo {organismo.nome} é {organismo.sequencia.percentual('GC'):.2f} %")
        #soma = organismo.sequencia.percentual('G') + organismo.sequencia.percentual('C')
        #print(f"O percentual de G+C do organismo {organismo.nome} é {soma} %")