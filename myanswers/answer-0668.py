from sklearn.feature_selection import VarianceThreshold

def filtrar_baja_varianza(X, p):
    threshold = p * (1 - p)
    selector = VarianceThreshold(threshold=threshold)
    expected = selector.fit_transform(X)
    
    return expected