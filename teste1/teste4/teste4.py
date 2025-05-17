
invoice_states = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Others': 19849.53
}

total_invoice = sum(invoice_states.values())

# % de cada state 
percents = {state: (value / total_invoice) * 100 for state, value in invoice_states.items()}

# Exibir os percentuais
for state, percent in percents.items():
    print(f"{state}: {percent:.2f}%")
