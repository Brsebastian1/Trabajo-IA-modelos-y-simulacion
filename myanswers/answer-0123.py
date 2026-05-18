from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

def evaluar_clasificador_riesgo(X, y):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Matriz de confusión: [[TN, FP], [FN, TP]]
    cm = confusion_matrix(y_test, y_pred)
    
    # Aseguramos que la matriz sea 2x2 para extraer los datos
    if cm.shape == (2, 2):
        fp = int(cm[0, 1])
        fn = int(cm[1, 0])
    else:
        # Caso borde si solo predice una clase
        fp = 0
        fn = 0
        
    metriz_dict = {
        'falsos_positivos': fp,
        'falsos_negativos': fn
    }
    
    # El output es la tupla (modelo, diccionario)
    output_data = (model, metriz_dict)
    
    return output_data