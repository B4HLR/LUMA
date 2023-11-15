from tensorflow.keras.models import load_model
import numpy as np

model = load_model('model.h5')

labels = open('labels.txt', 'r', encoding='utf-8').read().split('\n')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

# Classificar testo em uma entidade
def classfy(text):
    # Criar um array de entrada
    max_seq = 26 # Insira aqui o valor máximo real que você calculou anteriormente.
    x = np.zeros((1, max_seq, 256), dtype='float32')

    # Preencher o array com dados do texto
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        if k < max_seq:
            x[0, k, int(ch)] = 1.0
    
    # Fazer a previsão
    out = model.predict(x)
    idx = out.argmax()
    resu = str(idx2label[idx])
    return resu

'''
while True:
    text = input('Digite algo: ')
    print(classfy(text))
'''   
