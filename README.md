# Evaluador de Frases en Presente Simple

Este proyecto es una herramienta para evaluar la estructura gramatical de frases en presente simple en inglés. Utiliza TensorFlow y spaCy para analizar y verificar si una frase está correctamente estructurada en presente simple.

## Requisitos

Asegúrate de tener Python 3.7 o superior instalado en tu sistema. También necesitarás instalar las siguientes bibliotecas:

- `tensorflow`
- `spacy`
- `numpy`
- `pickle`

<hr>

# Instalacion


### Clona el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd <DIRECTORIO_DEL_PROYECTO>
```

### Crea un entorno virtual y actívalo:

```bash
python -m venv env
source env/bin/activate  # En Windows usa: env\Scripts\activate
```

### Instala los requisitos

```bash
pip install -r requirements.txt
```

### Descarga el modelo de spaCy:

```bash
python -m spacy download en_core_web_sm
```

> [!IMPORTANT]
> Se crean en "automatico" al ejecutar `train-model.py`
> Asegúrate de tener los archivos present_simple_model.keras, max_len.pkl y tokenizer.pkl en el mismo directorio que tu script principal.


### Ejecuta el script

```bash
python3 main.py
```

### Introduce una frase en presente simple cuando se te solicite:

```plaintext
Ingrese una frase en presente simple: She works in the morning
```

Estructura del Proyecto

* main.py: Script principal que contiene la lógica de preprocesamiento, predicción y evaluación de frases.
* present_simple_model.keras: Modelo de TensorFlow entrenado para la evaluación de frases en presente simple.
* tokenizer.pkl: Tokenizer utilizado para la conversión de texto en secuencias.
* requirements.txt: Archivo con las bibliotecas necesarias para el proyecto.

![image](https://github.com/user-attachments/assets/134d93c4-8e6a-418c-8637-3d6b5ec61524)


# Imagenes

### Analizis de mi archivo CSV

![image](https://github.com/user-attachments/assets/8383bd3a-6eef-49ef-a09e-8c4f538ba182)

### Ingreso de la oracion en ```present simple```

![image](https://github.com/user-attachments/assets/bb2f68a2-9626-487f-b94d-cf1dcfcb46d9)


### Errores 

![image](https://github.com/user-attachments/assets/2f1afaeb-4a84-43c2-8e46-c79446e47cf0)


### Video de uso (no audio)

[Muestra del uso del Sistema experto](https://youtu.be/meT2Ndt6mNc)





# ADIOS!

¡Gracias por utilizar este evaluador de frases en presente simple! Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto.
