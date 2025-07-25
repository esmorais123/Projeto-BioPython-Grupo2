from bio.ler_fasta import ler_fasta

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

organismo_do_fasta = ler_fasta(caminho_do_arquivo)

for organismo in organismo_do_fasta:
    print("sequencia: ", organismo.sequencia)
    