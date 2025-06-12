import random
import time

vida = 3
inventario = []
pontuacao = 0


def narrar(texto, velocidade=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidade)
    print()


def introducao():
    print("|--------|")
    print("|--------|")
    print("|--------|")
    print("|-O------| zzzzzzzzzz")
    print("|--------|")
    print("|--------|")
    print("|--------|")
    narrar("\U0001F680 *Som de portal abrindo*")
    narrar("Rick: Morty, acorda! Você derrubou meu controle de portais dentro da torradeira!")
    narrar("Morty: Aaaah, Rick, de novo não cara! Eu só queria... sei lá, dormir, sabe?")
    input("\n(Pressione ENTER para cair nessa aventura multiversal sem sentido...)")


def escolher_dimensao():
    narrar("\nVocê precisa escolher uma dimensão para procurar o controle:")
    print("1. Dimensão 35-C – Onde todo mundo é feito de queijo. \U0001F9C0")
    print("2. Dimensão Fart-X – Onde os peidos são conscientes e cantam ópera.")
    print("3. Cidadela dos Ricks – Centro político do multiverso.")
    escolha = input("Pra onde vamos, Morty? (1, 2 ou 3): ")
    return escolha.strip()


def batalha():
    global vida, pontuacao
    inimigos = [
        "um Jerry com superpoderes e autoestima altíssima",
        "um Meeseeks revoltado que virou gerente de banco",
        "um clone seu que acha que é o original",
        "um pepino armado até os dentes",
        "um Sr. Bundinha Cagada com acesso a Wi-Fi ilimitado"
    ]
    inimigo = random.choice(inimigos)
    narrar(f"\n\U0001F47E Enfrentamos {inimigo}!")

    narrar("Rick: Morty, escolha logo o que fazer!")
    print("1. Usar a Pistola de Portal invertida")
    print("2. Argumentar filosoficamente com o inimigo")
    print("3. Gritar e correr em círculos")
    escolha = input("Decida seu destino, Morty (1, 2 ou 3): ")

    resultado = random.randint(1, 3)
    if escolha == str(resultado):
        narrar("\u2705 FUNCIONOU! De algum jeito isso fez sentido no multiverso.")
        item = random.choice([
            "Mini Meeseeks de bolso", 
            "Cabelo do Rick (falso)", 
            "Portal engarrafado", 
            "Pingente do Squanchy", 
            "Fidget Spinner Interdimensional"
        ])
        inventario.append(item)
        pontuacao += 10
        narrar(f"\U0001F381 Você ganhou um item: {item}")
    else:
        vida -= 1
        pontuacao -= 5
        narrar("\U0001F4A5 Isso deu completamente errado, Morty!")
        narrar(f"Rick: Você perdeu uma vida. Vidas restantes: {vida}")
        if vida == 0:
            narrar("\n\u2620\ufe0f Você virou poeira quântica. Rick te reconstrói com DNA de barata.")
            narrar("Rick: Fica até melhor que o original. Tsc.")
            exit()


def evento_aleatorio():
    global pontuacao, inventario  
    narrar("\n\U0001F3B2 Evento interdimensional ativado!")
    eventos = [
        "Morty entra num bar com dezenas de Mortys... todos reclamando da vida.",
        "Rick tropeça e acidentalmente cria uma IA que ama jazz.",
        "Você encontra o Cão Snuffles pilotando uma nave e ele te ignora por completo.",
        "Birdperson aparece, diz algo profundo, e vai embora voando lentamente.",
        "Um Gromflomite oferece um emprego estável em troca da sua alma."
    ]
    narrar(random.choice(eventos))
    inventario.append("Trauma existencial leve")
    pontuacao += 5


def fase_bonus():
    global pontuacao, vida
    narrar("\n\U0001F952 *Pickle Rick aparece gritando e girando com facas*")
    narrar("Pickle Rick: Você quer bônus, Morty? ENTÃO VAMOS LUTAR!")
    print("1. Lutar com ketchup")
    print("2. Fugir para a banheira")
    print("3. Se disfarçar de pepino também")
    escolha = input("Escolha rápida, Morty (1, 2 ou 3): ")
    if escolha == "3":
        narrar("Pickle Rick respeita sua coragem... e te poupa.")
        pontuacao += 20
    else:
        narrar("Pickle Rick te lança contra a parede, mas você sobrevive.")
        vida -= 1



def final():
    narrar("\n\U0001F9EA De volta ao laboratório...")
    if "Portal engarrafado" in inventario:
        narrar("Rick: Finalmente! Isso vai servir pra... hmm... nada útil. Mas parece legal.")
        narrar("\U0001F3C6 Final secreto: ‘Colecionador de Itens Inúteis do Multiverso’")
    else:
        narrar("Rick: Bom, pelo menos recuperamos o controle de portais. E você só morreu duas vezes!")
    narrar(f"\nPontuação final: {pontuacao} pontos")
    narrar("Morty: Rick... isso tudo foi real?")
    narrar("Rick: Morty, nada é real. Inclusive esse script.")
    narrar("\n\U0001F389 FIM! Vá descansar, já é loucura o suficiente por hoje.")


def jogar():
    introducao()
    for rodada in range(3):
        escolha = escolher_dimensao()
        if escolha in ["1", "2", "3"]:
            batalha()
            if random.choice([True, False]):
                evento_aleatorio()
        else:
            narrar("Rick: Você digitou errado, Morty. Agora estamos numa dimensão onde tudo é suco de cacto.")
            return
    fase_bonus()
    final()
    print("\n\U0001F9F3 Inventário final:", ", ".join(inventario))

if __name__ == "__main__":
    jogar()
