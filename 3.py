import json

with open('faturamento.json') as f:
    faturamento = json.load(f)

faturamento = [dia for dia in faturamento if dia > 0]

# Cálculos
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = len([dia for dia in faturamento if dia > media_mensal])

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
