from collections import defaultdict
from collections import Counter

texto1 = """Provavelmente, ao construir um website, você já deve ter reparado que muitos dos valores nos arquivos CSS são dados que se repetem constantemente, não é mesmo? Por exemplo, a paleta de cores que mantém o padrão visual da página é reutilizada em inúmeros pontos do código. Sendo assim, fazer a manutenção do projeto e alterar esses valores manualmente pode se tornar uma tarefa trabalhosa e passiva de erros, ainda mais em aplicações de grande escala. Mas então, como podemos melhorar essa situação? Uma boa alternativa é utilizar as Variáveis no CSS como aliadas! Se você ficou interessado e deseja descobrir como fazer isso, vem comigo que nesse artigo eu te ensinarei mais sobre esse assunto detalhadamente."""

texto2 = """Você já deve ter preenchido um formulário que não indicava claramente o porquê de algum campo não estar válido e teve que ficar adivinhando quantos caracteres sua senha precisava ter ou que tipo de caracteres deveria receber. Ou, em um formulário longo, já ocorreu de preencher apenas os campos que achava serem requeridos e só no final, ao tentar submeter os dados, se deparou com inúmeras mensagens de erro mostrando que diversos outros campos eram obrigatórios? Chato, né? Vem aprender como melhorar essa experiência com o uso das validações customizadas do Angular!"""

print("Counter(texto1.lower()):", Counter(texto1.lower()))

aparicoes = Counter(texto1.lower())
print("sum(aparicoes.values()):", sum(aparicoes.values()))

total = sum(aparicoes.values())

lista = [(letra, frequencia/total) for letra, frequencia in aparicoes.items()]
print(lista)

lista = dict(lista)
print(lista)

lista = Counter(dict(lista))
print("lista.most_common():", lista.most_common(3))

def analisar(texto):
    aparicoes = Counter(texto.lower())
    total = sum(aparicoes.values())
    lista = [(letra, frequencia/total) for letra, frequencia in aparicoes.items()]
    lista = Counter(dict(lista))
    for char, proporcao in lista.most_common(5):
        print( "{} => {:.2f}%".format(char, proporcao * 100))

analisar(texto2)