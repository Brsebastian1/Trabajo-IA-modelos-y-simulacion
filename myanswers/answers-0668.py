import numpy as np
from sklearn.cluster import KMeans

def segmentar_y_calcular_distancias(X, n_clusters):

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    labels = model.fit_predict(X)
    centroids = model.cluster_centers_
    
    # Calcular distancias manualmente para el output esperado
    distancias = []
    for i in range(len(X)):
        punto = X[i]
        centroide_asignado = centroids[labels[i]]
        # Distancia euclidiana: raiz de la suma de los cuadrados de las diferencias
        d = np.linalg.norm(punto - centroide_asignado)
        distancias.append(d)
    
    input_data = {
        'X': X,
        'n_clusters': n_clusters
    }
    output_data = (labels, np.array(distancias))
    
    return output_data