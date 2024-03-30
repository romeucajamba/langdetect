from langdetect import detect

text = str(input("Digite a palavra ou frase: "))

print(detect(text))