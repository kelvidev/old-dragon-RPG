from attributeRoller import AttributeRoller
from character import Character
ATTRIBUTE_NAMES = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
class RPGGenerator:
    
    def __init__(self):
        self.characters = []

    def menu(self):
            while True:
                print("\nEscolha o estilo de geração de atributos:")
                print("  1) Estilo Clássico (3d6, atribui na ordem)")
                print("  2) Estilo Aventureiro (3d6, distribua como quiser)")
                print("  3) Estilo Heroico (4d6 drop lowest, distribua como quiser)")
                print("  4) Sair")
                choice = input("Opção: ").strip()
                match choice:
                    case "1":
                        self.style_flow("classico")
                    case "2":
                        self.style_flow("aventureiro")
                    case "3":
                        self.style_flow("heroico")
                    case "4":
                        print("Saindo. Até mais!")
                        break
                    case _:
                        print("Opção inválida — tente novamente.")

    def style_flow(self, style):
        while True:
            print(f"\n--- MODO: {style.capitalize()} ---")
            print("  1) Criar personagem")
            print("  2) Listar personagens criados")
            print("  3) Voltar ao menu de estilos")
            choice = input("Opção: ").strip()
            if choice == "1":
                self.create_character(style)
            elif choice == "2":
                self.list_characters()
            elif choice == "3":
                return
            else:
                print("Opção inválida — tente novamente.")

    def create_character(self, style):
        name = input("Nome do personagem: ").strip()
        if not name:
            name = "SemNome"

        rolls = AttributeRoller.generate(style)
        print("\nRolagens realizadas (6 valores):")
        for i, v in enumerate(rolls, start=1):
            print(f"  [{i}] {v}")
        
        if style == "classico":
            attributes = {ATTRIBUTE_NAMES[i]: rolls[i] for i in range(6)}
            char = Character(name, style, attributes)
            self.characters.append(char)
            print("\nPersonagem criado (atributos atribuídos na ordem clássica):")
            print(char)
            return

        attributes = {}
        available_indices = set(range(1,7))  # 1..6
        print("\nAgora distribua os 6 valores para os atributos.")
        print("Informe o número da rolagem (1..6) que deseja atribuir a cada atributo.")
        print("Exemplo: se quiser dar o valor da rolagem [3] para Força, digite 3.")
        for attr in ATTRIBUTE_NAMES:
            while True:
                try:
                    choice = input(f"Escolha índice para '{attr}': ").strip()
                    idx = int(choice)
                    if idx < 1 or idx > 6:
                        print("Índice fora do intervalo (1..6). Tente novamente.")
                        continue
                    if idx not in available_indices:
                        print("Índice já usado. Escolha outro.")
                        continue
                    attributes[attr] = rolls[idx-1]
                    available_indices.remove(idx)
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro (1..6).")

        char = Character(name, style, attributes)
        self.characters.append(char)
        print("\nPersonagem criado com sucesso:")
        print(char)

    def list_characters(self):
        if not self.characters:
            print("\nNenhum personagem criado ainda.")
            return
        print("\n--- Personagens Criados ---")
        for i, c in enumerate(self.characters, start=1):
            print(f"\n[{i}]")
            print(c)
