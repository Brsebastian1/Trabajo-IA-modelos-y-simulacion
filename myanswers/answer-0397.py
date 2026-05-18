from sklearn.ensemble import IsolationForest

def detectar_anomalias_murcielagos(df, contaminacion):

    input_data = {'df': df.copy(), 'contaminacion': contaminacion}
    
    df_clean = df.copy()
    df_clean['frecuencia_pico'] = df_clean['frecuencia_pico'].rolling(window=3).mean()
    df_clean = df_clean.dropna()
    X = df_clean[['frecuencia_pico', 'duracion_pulso']].values
    iso = IsolationForest(contamination=contaminacion, random_state=42)
    preds = iso.fit_predict(X)
    
    output_data = preds
    return output_data