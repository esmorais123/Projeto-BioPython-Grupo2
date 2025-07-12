

from bio.ler_fasta import ler_fasta

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

organismo_do_fasta = ler_fasta(caminho_do_arquivo)

print ("Os organismos desse arquivo fasta são: ")
for organismo in organismo_do_fasta:
    print(organismo.nome)
