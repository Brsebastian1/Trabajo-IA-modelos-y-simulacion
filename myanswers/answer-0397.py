import pandas as pd

def calcular_metricas_clientes(df, contaminacion):
    metricas_cliente = df.groupby("cliente_id").agg(
        total_gastado_cliente=("monto", "sum"),
        promedio_gasto_cliente=("monto", "mean"),
        num_transacciones_cliente=("monto", "count")
    ).reset_index()

    # Métricas por cliente y categoría
    metricas_categoria = df.groupby(["cliente_id", "categoria"]).agg(
        total_categoria=("monto", "sum")
    ).reset_index()

    # Merge
    resultado = metricas_categoria.merge(
        metricas_cliente,
        on="cliente_id",
        how="left"
    )

    # Calcular porcentaje
    resultado["porcentaje_categoria"] = (
        resultado["total_categoria"] /
        resultado["total_gastado_cliente"]
    )

    # Ordenar
    resultado = resultado.sort_values(
        by=["cliente_id", "categoria"]
    ).reset_index(drop=True)

    output_data = resultado

    return output_data