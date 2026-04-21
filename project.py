import pandas as pd
import matplotlib.pyplot as plt

def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except FileNotFoundError:
        print(f"Erro: arquivo '{file}' não encontrado.")
        return None

def calculate_totals(df):
    df["total"] = df["preco"] * df["quantidade"]
    print(df)
    print()

    max_venda = df["total"].max()

    idx = df["total"].idxmax()
    print(f"{df.loc[idx,'produto']} foi o produto que mais vendeu, com R${max_venda:.2f} em vendas!")
    print()

    return df

def show_results(df):
    total_geral = sum(df["total"])
    print(f"O total geral de vendas é de: R${total_geral:.2f}")
    print()

    vendas_categoria = df.groupby("categoria")["total"].sum()
    print(f"Total de vendas de cada categoria:")
    for categoria, valor in vendas_categoria.items():
        print(f" {categoria}: R${valor:.2f}")

def generate_chart(df):

    plt.bar(df["produto"], df["total"])
    plt.title("Total de Vendas por Produto")
    plt.xlabel("Produtos")
    plt.ylabel("Vendas")
    plt.savefig("sales_infograph.png")
    plt.show()

df = load_data("sales.csv")
if df is not None:
    calculate_totals(df)
    show_results(df)
    generate_chart(df)
