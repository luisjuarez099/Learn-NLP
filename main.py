# main.py

from analizador import analyze_past_spacy, analyze_present_spacy, analyze_gerund_or_present_participle_spacy

def main():
    # Menú para seleccionar las palabras a analizar
    print("Welcome to the sentence analyzer")
    print("1. Analyze present simple")
    print("2. Analyze past simple")
    print("3. Analyze gerund or present participle")
    print("4. Run predefined tests")

    option = input("Select an option: ")
    if option == "1":
        data_words = input("Enter a sentence: ")
        print(analyze_present_spacy(data_words))
    elif option == "2":
        data_words = input("Enter a sentence: ")
        print(analyze_past_spacy(data_words))
    elif option == "3":
        data_words = input("Enter a sentence: ")
        print(analyze_gerund_or_present_participle_spacy(data_words))
    elif option == "4":
        print(analyze_past_spacy("She played soccer last summer."))
        print()
        print(analyze_present_spacy("He plays soccer every summer."))
        print()
        print(analyze_gerund_or_present_participle_spacy("She is playing soccer right now."))
    else:
        print("Invalid option. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
