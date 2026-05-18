import pandas as pd

def analizar_variacion_precios(df):
    df_sol = df.copy()
    df_sol['fecha'] = pd.to_datetime(df_sol['fecha'])
    df_sol = df_sol.sort_values(['producto_id', 'fecha'])
    
    # Calculamos el cambio agrupando por producto
    df_sol['cambio_precio'] = df_sol.groupby('producto_id')['precio'].diff()
    df_sol['es_subida'] = df_sol['cambio_precio'] > 0
    
    # Quitamos nulos y reseteamos índice
    df_sol = df_sol.dropna(subset=['cambio_precio']).reset_index(drop=True)
    
    output_data = df_sol
    
    return output_data