import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

df["total"] = df["preco"] * df["quantidade"]
print(df)
print()
max_venda = df["total"].max()

idx = df["total"].idxmax()
print(f"{df.loc[idx,"produto"]} foi o produto que mais vendeu, com R${max_venda:.2f} em vendas!")
print()

total_geral = sum(df["total"])
print(f"O total geral de vendas é de: R${total_geral:.2f}")
print()

vendas_categoria = df.groupby("categoria")["total"].sum()
print(f"Total de vendas de cada categoria:")
for categoria, valor in vendas_categoria.items():
    print(f" {categoria}: R${valor:.2f}")

plt.bar(df["produto"], df["total"])
plt.title("Total de Vendas por Produto")
plt.xlabel("Produtos")
plt.ylabel("Vendas")
plt.savefig("gráfico vendas.png")
plt.show()