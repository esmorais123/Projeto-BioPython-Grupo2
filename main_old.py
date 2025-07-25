from bio.ler_fasta import ler_fasta

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

organismos_fasta = ler_fasta(caminho_do_arquivo)
organismos_ordenados = sorted(organismos_fasta, key=lambda o: o.nome)

print("Os organismos desse arquivo FASTA são:\n")

for organismo in organismos_fasta:
    print(organismo.nome)
    print("Tamanho: ", organismo.sequencia.calcular_tamanho())