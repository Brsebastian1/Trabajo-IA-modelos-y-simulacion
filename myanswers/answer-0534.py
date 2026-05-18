import numpy as np
import pandas as pd

def agrupar_eventos_por_franja(df):
    input_data = {"df": df.copy()}

    output_df = df.copy()
    output_df["fecha_hora"] = pd.to_datetime(output_df["fecha_hora"])

    horas = output_df["fecha_hora"].dt.hour
    output_df["franja"] = np.select(
        [
            horas.between(0, 5),
            horas.between(6, 11),
            horas.between(12, 17),
            horas.between(18, 23),
        ],
        ["madrugada", "mañana", "tarde", "noche"],
        default="noche",
    )

    output_df = (
        output_df.groupby(["franja", "categoria"], as_index=False)
        .agg(total_monto=("monto", "sum"), num_eventos=("monto", "size"))
    )

    orden = ["madrugada", "mañana", "tarde", "noche"]
    output_df["franja"] = pd.Categorical(output_df["franja"], categories=orden, ordered=True)

    output_df = output_df.sort_values(by=["franja", "categoria"]).reset_index(drop=True)
    output_df["total_monto"] = output_df["total_monto"].round(2)

    return output_df