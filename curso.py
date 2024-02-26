import os 
import pandas as pd
import plotly.express as px
lista_arquivo = os.listdir(r"C:\Users\pcyes\OneDrive\Área de Trabalho\curso basico python\venda")
tabela_total = pd.DataFrame()
for arquivo in lista_arquivo:
        print(fr"C:\Users\pcyes\OneDrive\Área de Trabalho\curso basico python\venda")

        if "Vendas" in arquivo:
            print(fr"C:\Users\pcyes\OneDrive\Área de Trabalho\curso basico python\venda")


tabela = pd.read_csv(fr"C:\Users\pcyes\OneDrive\Área de Trabalho\curso basico python\venda /{arquivo}")
tabela_total = pd.concat([tabela_total, tabela])
print(tabela_total)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]]. sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)
tabela_total ["Faturamento"]= tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]]. sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)
tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]]
print(tabela_lojas)

grafico = px.bar(tabela_lojas,x= tabela_lojas.index ,y="Faturamento")
grafico.show()