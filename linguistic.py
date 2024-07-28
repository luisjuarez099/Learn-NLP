# linguistic.py

import spacy
from grammar_rules import past_verbs, present_verbs, gerunds, grammar_rules, past_participle_verbs

# Cargar el modelo de spaCy
nlp = spacy.load("en_core_web_sm")

def is_past_simple_spacy(sentence):
    doc = nlp(sentence)
    for token in doc:
        # Verificar si el token es un verbo en pasado
        if token.tag_ == "VBD":
            # Verificar si el verbo está en la lista de verbos en pasado
            if token.lemma_ in past_verbs or token.text in past_verbs:
                return True, f"'{token.text}' is a past simple verb."
    return False, "No past simple verbs found."

def is_present_simple_spacy(sentence):
    doc = nlp(sentence)
    for token in doc:
        # Verificar si el token es un verbo en presente simple
        if token.tag_ in ["VBZ", "VBP"]:
            # Verificar si el verbo está en la lista de verbos en presente simple
            if token.lemma_ in present_verbs or token.text in present_verbs:
                return True, f"'{token.text}' is a present simple verb."
    return False, "No present simple verbs found."

def is_gerund_or_present_participle_spacy(sentence):
    doc = nlp(sentence)
    for token in doc:
        # Verificar si el token es un verbo en gerundio o participio presente
        if token.tag_ == "VBG":
            # Verificar si el verbo está en la lista de gerundios
            if token.lemma_ in gerunds or token.text in gerunds:
                return True, f"'{token.text}' is a gerund or present participle verb."
    return False, "No gerund or present participle verbs found."

def is_past_participle_spacy(sentence):
    doc = nlp(sentence)
    for token in doc:
        if token.tag_ == "VBN":
            return True, f"'{token.text}' is a past participle verb."
    return False, "No past participle verbs found."


def explain_grammar(rule_name):
    rule = grammar_rules.get(rule_name, None)
    if rule:
        return rule["description"], rule["structure"], rule["examples"]
    else:
        return "No explanation found for this rule."
