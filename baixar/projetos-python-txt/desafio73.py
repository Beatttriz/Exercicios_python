times=('Palmeiras','Flamengo','Vasco', 'Botafogo', 'Fluminense')

print(f'Lista de times do Brasileirão: {times}')
print(f'Os 3 primeiros são {times[0:3]}')
print(f'Os dis últimos são {times[-2:]}')
print(f'Em ordem alfabética {sorted(times)}')
print(f'O vasco está na {times.index("Vasco")+1}º posição')