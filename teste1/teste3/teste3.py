import json

invoice_json = '''
{
    "days": [
        {"day": 1, "value": 500},
        {"day": 2, "value": 1000},
        {"day": 3, "value": 750},
        {"day": 4, "value": 2000},
        {"day": 5, "value": 1200},
        {"day": 6, "value": 0},
        {"day": 7, "value": 1500}
    ]
}
'''

dados = json.loads(invoice_json)
invoice = [day["value"] for day in dados["days"] if day["value"] > 0]

min_invoice = min(invoice)
max_invoice = max(invoice)
avrg_invoice = sum(invoice) / len(invoice)

# invoice acima da media
days_acima_meday = sum(1 for value in invoice if value > avrg_invoice)

# Exibir resultados
print(f"Menor faturamento: R${min_invoice}")
print(f"Maior faturamento: R${max_invoice}")
print(f"Número de dias acima da media: {days_acima_meday}" + " dias")
