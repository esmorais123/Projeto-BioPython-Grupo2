from bio.ler_fasta import ler_fasta

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

organismo_do_fasta = ler_fasta(caminho_do_arquivo)

for organismo in organismo_do_fasta:
    print("sequência original:", organismo.sequencia)
    print("proteína traduzida:", organismo.traduzir(parar=False))
