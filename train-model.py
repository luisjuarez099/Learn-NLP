import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
import pandas as pd
import numpy as np
import spacy
import pickle

# Cargar datos
df = pd.read_csv('phrases.csv')
phrases = df['phrase'].values
labels = df['label'].values

# Preprocesamiento
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_stop])

processed_phrases = [preprocess_text(phrase) for phrase in phrases]

# Crear vocabulario
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(processed_phrases)
X = tokenizer.texts_to_sequences(processed_phrases)
X = tf.keras.preprocessing.sequence.pad_sequences(X)

# Save the maximum length used for padding
max_len = X.shape[1]

# Modelo
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64),
    LSTM(64),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, np.array(labels), epochs=150, batch_size=32)

# Guardar el modelo en el nuevo formato
model.save('present_simple_model.keras')

# Guardar el tokenizer y max_len
with open('tokenizer.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('max_len.pkl', 'wb') as handle:
    pickle.dump(max_len, handle, protocol=pickle.HIGHEST_PROTOCOL)