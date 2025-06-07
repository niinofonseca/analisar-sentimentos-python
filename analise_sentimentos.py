
import json
import string

RED = '\033[31m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
PURPLE = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

palavras_positivas = {
    'bom', 'legal', 'ótimo', 'excelente', 'maravilhoso', 'satisfatório',
    'confiável', 'gentil', 'show', 'top', 'irado', 'amei', 'adorei', 'gostei',
    'perfeito', '10', '100', '1000'
}

palavras_negativas = {
    'ruim', 'péssimo', 'horrível', 'decepcionante', 'lixo', 'insatisfatório',
    'precário', 'falho', 'limitado', 'confuso', 'desorganizado', 'bosta',
    'tosco', 'zoado', 'chato', 'porcaria', 'treta', 'furada', '0'
}

positivas_peso1 = {
    "termos": [
        'bom', 'legal', 'satisfatório', 'confiável', 'gentil', 'show',
        'gostei', '10'
    ],
    "peso":
    1
}

positivas_peso2 = {
    "termos": [
        'ótimo', 'excelente', 'maravilhoso', 'top', 'irado', 'amei', 'adorei',
        'perfeito', '100', '1000'
    ],
    "peso":
    2
}

negativas_peso1 = {
    "termos": [
        'ruim', 'insatisfatório', 'precário', 'falho', 'limitado', 'confuso',
        'desorganizado', 'chato', 'furada'
    ],
    "peso":
    1
}

negativas_peso2 = {
    "termos": [
        'péssimo', 'horrível', 'decepcionante', 'lixo', 'bosta', 'tosco',
        'zoado', 'porcaria', 'treta', '0'
    ],
    "peso":
    2
}


def verifica_quantia_positivas(comentario):
   comentario = comentario.lower()
   comentario = comentario.translate(str.maketrans('', '', string.punctuation))
   palavras_comentario = comentario.split()

   termos_positivos = []

   for palavra in palavras_comentario:
      if palavra in palavras_positivas:
         termos_positivos.append(palavra)

   return termos_positivos


def verifica_quantia_positivas_negacao(comentario):
    comentario = comentario.lower()
    comentario = comentario.translate(str.maketrans('', '', string.punctuation))
    palavras_comentario = comentario.split()

    termos_positivos = []
    positiva_negada = None

    i = 0
    while i < len(palavras_comentario):
        palavra = palavras_comentario[i]

        if palavra == 'não' and i + 1 < len(palavras_comentario):
            for j in range(i + 1, len(palavras_comentario)):
                proxima_palavra = palavras_comentario[j]
                if proxima_palavra in palavras_positivas:
                    positiva_negada = proxima_palavra
                    i = j 
                    break
        elif palavra in palavras_positivas:
            termos_positivos.append(palavra)

        i += 1

    return termos_positivos, positiva_negada

def verifica_quantia_negativas(comentario):
   comentario = comentario.lower()
   comentario = comentario.translate(str.maketrans('', '', string.punctuation))
   palavras_comentario = comentario.split()

   termos_negativos = []

   for palavra in palavras_comentario:
      if palavra in palavras_negativas:
         termos_negativos.append(palavra)

   return termos_negativos


def verifica_quantia_negativas_negacao(comentario):
    comentario = comentario.lower()
    comentario = comentario.translate(str.maketrans('', '', string.punctuation))
    palavras_comentario = comentario.split()

    termos_negativos = []
    negativa_negada = None

    i = 0
    while i < len(palavras_comentario):
        palavra = palavras_comentario[i]

        if palavra == 'não' and i + 1 < len(palavras_comentario):
            for x in range(i + 1, len(palavras_comentario)):
                proxima_palavra = palavras_comentario[x]
                if proxima_palavra in palavras_negativas:
                    negativa_negada = proxima_palavra
                    i = x  
                    break
        elif palavra in palavras_negativas:
            termos_negativos.append(palavra)

        i += 1

    return termos_negativos, negativa_negada


def define_peso_positivo(termos_positivos):
   peso_positivo = 0

   for termo in termos_positivos:
      if termo in positivas_peso1["termos"]:
         peso_positivo += positivas_peso1["peso"]
      elif termo in positivas_peso2["termos"]:
         peso_positivo += positivas_peso2["peso"]

   return peso_positivo


def define_peso_positivo_negacao(termos_positivos, positiva_negada):
   peso_positivo = 0

   for termo in termos_positivos:
      if termo in positivas_peso1["termos"]:
         peso_positivo += positivas_peso1["peso"]
      elif termo in positivas_peso2["termos"]:
         peso_positivo += positivas_peso2["peso"]
   
   if positiva_negada in positivas_peso1["termos"]:
      peso_positivo -= positivas_peso1["peso"]
   elif positiva_negada in positivas_peso2["termos"]:
      peso_positivo -= positivas_peso2["peso"]

   return peso_positivo


def define_peso_negativo(termos_negativos):
   peso_negativo = 0

   for termo in termos_negativos:
      if termo in negativas_peso1["termos"]:
         peso_negativo += negativas_peso1["peso"]
      elif termo in negativas_peso2["termos"]:
         peso_negativo += negativas_peso2["peso"]

   return peso_negativo


def define_peso_negativo_negacao(termos_negativos, negativa_negada):
   peso_negativo = 0

   for termo in termos_negativos:
      if termo in negativas_peso1["termos"]:
         peso_negativo += negativas_peso1["peso"]
      elif termo in negativas_peso2["termos"]:
         peso_negativo += negativas_peso2["peso"]
   
   if negativa_negada in negativas_peso1["termos"]:
      peso_negativo -= negativas_peso1["peso"]
   elif negativa_negada in negativas_peso2["termos"]:
      peso_negativo -= negativas_peso2["peso"]

   return peso_negativo


def classifica_comentario(peso_positivo, peso_negativo):
   if peso_positivo > peso_negativo:
      return (GREEN + "\nEsse comentário é positivo\n" + RESET)
   elif peso_negativo > peso_positivo:
      return (RED + "\nEsse comentário é negativo\n" + RESET)
   else:
      return (YELLOW + "\nEsse comentário é neutro ou ambíguo\n" + RESET)


def classifica_lista_comentario(lista_json):
   lista_comentarios = json.loads(lista_json)

   for chave, comentario in lista_comentarios.items():
      if 'não' in comentario:
            termos_positivos, positiva_negada = verifica_quantia_positivas_negacao(comentario)
            termos_negativos, negativa_negada = verifica_quantia_negativas_negacao(comentario)
            peso_positivo = define_peso_positivo_negacao(termos_positivos, positiva_negada)
            peso_negativo = define_peso_negativo_negacao(termos_negativos, negativa_negada)
            resultado = classifica_comentario(peso_positivo, peso_negativo)
      else:
         termos_positivos = verifica_quantia_positivas(comentario)
         termos_negativos = verifica_quantia_negativas(comentario)
         peso_positivo = define_peso_positivo(termos_positivos)
         peso_negativo = define_peso_negativo(termos_negativos)
         resultado = classifica_comentario(peso_positivo, peso_negativo)

      print(f"\nComentário {chave}: ")
      print(resultado)


def main():
   print(BOLD + BLUE + "\nEsse é um sistema de análise de sentimentos.\n" +
         RESET)

   while True:
      opcao = int(input(BOLD + BLUE + "\nEscolha:" + YELLOW + "\n1-Analisar 1 comentário\n2-Analisar lista de comentário (JSON)" + PURPLE + "\n3-Sair" + BLUE + "\nOpção:  " + RESET))

      if opcao == 1:
         comentario = input("Digite um comentário: ")

         if 'não' in comentario:
            termos_positivos, positiva_negada = verifica_quantia_positivas_negacao(comentario)
            termos_negativos, negativa_negada = verifica_quantia_negativas_negacao(comentario)
            peso_positivo = define_peso_positivo_negacao(termos_positivos, positiva_negada)
            peso_negativo = define_peso_negativo_negacao(termos_negativos, negativa_negada)
            resultado = classifica_comentario(peso_positivo, peso_negativo)
            print(resultado)
         else:
            termos_positivos = verifica_quantia_positivas(comentario)
            termos_negativos = verifica_quantia_negativas(comentario)
            peso_positivo = define_peso_positivo(termos_positivos)
            peso_negativo = define_peso_negativo(termos_negativos)
            resultado = classifica_comentario(peso_positivo, peso_negativo)
            print(resultado)

      elif opcao == 2:
         lista_json = input("Digite uma lista de comentários em formato JSON: ")
         classifica_lista_comentario(lista_json)
      elif opcao == 3:
         break

main()

#{"1": "esse produto é excelente e muito confiável.","2": "gostei muito do atendimento, foi perfeito!","3": "péssimo serviço, totalmente decepcionante.","4": "esse lugar é horrível, não gostei nada.","5": "o produto é bom, mas o atendimento foi confuso.","6": "não gostei muito, mas também não é péssimo."}

#- Comentário 1: Positivo 
#- Comentário 2: Positivo 
#- Comentário 3: Negativo
#- Comentário 4: Negativo 
#- Comentário 5: Neutro 
#- Comentário 6: Positivo
