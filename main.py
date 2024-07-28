import tensorflow as tf
import spacy
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Cargar el modelo y tokenizer
model = tf.keras.models.load_model('present_simple_model.keras')

with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

with open('max_len.pkl', 'rb') as handle:
    max_len = pickle.load(handle)

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_stop])

def predict(phrase):
    processed_phrase = preprocess_text(phrase)
    sequence = tokenizer.texts_to_sequences([processed_phrase])
    padded_sequence = pad_sequences(sequence, maxlen=max_len)  # Use max_len for padding
    prediction = model.predict(padded_sequence)
    return prediction[0][0] > 0.5

def evaluate_phrase(phrase):
    if predict(phrase):
        return "La frase está correctamente estructurada en presente simple."
    else:
        return "La frase tiene errores. Asegúrate de usar la estructura correcta: Sujeto + Verbo + Objeto."

# Ejemplo de uso
user_input = input("Ingrese una frase en presente simple: ")
print(evaluate_phrase(user_input))