# analyzer.py

from linguistic import is_past_simple_spacy, is_present_simple_spacy, is_gerund_or_present_participle_spacy

def analyze_past_spacy(sentence):
    is_past, explanation = is_past_simple_spacy(sentence)
    if is_past:
        return f"The sentence '{sentence}' is in past simple. {explanation}"
    else:
        return f"The sentence '{sentence}' is not in past simple. {explanation}"
    
def analyze_present_spacy(sentence):
    is_present, explanation = is_present_simple_spacy(sentence)
    if is_present:
        return f"The sentence '{sentence}' is in present simple. {explanation}"
    else:
        return f"The sentence '{sentence}' is not in present simple. {explanation}"

def analyze_gerund_or_present_participle_spacy(sentence):
    is_gerund, explanation = is_gerund_or_present_participle_spacy(sentence)
    if is_gerund:
        return f"The sentence '{sentence}' contains a gerund or present participle. {explanation}"
    else:
        return f"The sentence '{sentence}' does not contain a gerund or present participle. {explanation}"
