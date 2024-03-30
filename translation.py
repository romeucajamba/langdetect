from langdetect import detect_langs

text = str(input("Digite uma frase e vê qual é o idoma: "))

languages = detect_langs(text)

for lang in languages:
    print("Idioma:", lang.lang, "| Probabilidade:", lang.prob)
