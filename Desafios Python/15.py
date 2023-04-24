dias_aluguel = float(input('Por quantos dias o carro foi alugado? '))
km_rodados = float(input('Quantos quilômetros foram rodados? '))
total_pagar = (dias_aluguel * 60) + (km_rodados * 0.15)
print(f'O total a pagar é de R${total_pagar:.2f}')