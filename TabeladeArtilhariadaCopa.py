jogos = int(input("Quantos jogos ele disputou? "))
total_gols = 0
em_branco = 0

for i in range(1, jogos + 1):
    gols = int(input(f"Gols no jogo {i}: "))
    total_gols += gols
    if gols == 0:
        em_branco += 1

media = total_gols / jogos if jogos > 0 else 0

print("\n--- Resultado ---")
print(f"Total de gols: {total_gols}")
print(f"Média por jogo: {media:.2f}")
print(f"Jogos sem marcar: {em_branco}")
