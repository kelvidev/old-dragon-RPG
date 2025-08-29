# main.py
from attributeRoller import AttributeRoller
from characterBase import Character
from human import Human
from elf import Elf
from dwarf import Dwarf
from halfling import Halfling
from academico import Academic
from druid import Druid
from thief import Thief
import types

ATTRIBUTE_NAMES = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

# Dicionários para mapear escolhas
AVAILABLE_RACES = {
    "1": Human,
    "2": Elf,
    "3": Dwarf,
    "4": Halfling
}

AVAILABLE_CLASSES = {
    "1": Academic,
    "2": Druid,
    "3": Thief
}

def create_character_with_race_and_class(name, style, attributes, race_class, char_class):
    """
    Cria um personagem combinando dinamicamente a classe base Character
    com uma raça específica usando herança múltipla dinâmica.
    """
    # Cria uma nova classe que herda de Character e da raça escolhida
    DynamicCharacter = type(
        f"Character{race_class.name}",
        (Character, race_class),
        {}
    )
    
    # Instancia o personagem com a classe combinada
    character = DynamicCharacter(name, style, attributes, char_class)
    
    return character

class RPGGenerator:
    
    def __init__(self):
        self.characters = []

    def menu(self):
        while True:
            print("\n" + "="*50)
            print("🎲 GERADOR DE PERSONAGENS RPG 🎲")
            print("="*50)
            print("Escolha o estilo de geração de atributos:")
            print("  1) Estilo Clássico (3d6, atribui na ordem)")
            print("  2) Estilo Aventureiro (3d6, distribua como quiser)")
            print("  3) Estilo Heroico (4d6 drop lowest, distribua como quiser)")
            print("  4) Sair")
            print("-" * 50)
            
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
                    print("❌ Opção inválida — tente novamente.")

    def style_flow(self, style):
        while True:
            print(f"\n--- MODO: {style.upper()} ---")
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
                print("❌ Opção inválida — tente novamente.")

    def select_race(self):
        """Permite ao usuário escolher uma raça."""
        while True:
            print("\n📖 Escolha a raça do personagem:")
            print("  1) Humano")
            print("  2) Elfo")
            print("  3) Anão")
            print("  4) Halfling")
            
            choice = input("Raça: ").strip()
            if choice in AVAILABLE_RACES:
                race_class = AVAILABLE_RACES[choice]
                print(f"✅ Raça selecionada: {race_class.name}")
                return race_class
            else:
                print("❌ Opção inválida. Tente novamente.")

    def select_class(self, race_class):
        """Permite ao usuário escolher uma classe."""
        while True:
            print("\n⚔️ Escolha a classe do personagem:")
            print("  1) Acadêmico")
            print("  2) Druida")
            print("  3) Ladrão")
            
            choice = input("Classe: ").strip()
            if choice in AVAILABLE_CLASSES:
                char_class = AVAILABLE_CLASSES[choice]()
                
                if hasattr(char_class, 'allowed_alignment'):
                    race_instance = race_class()
                    if not char_class.allowed_alignment(race_instance.alignment):
                        print(f"⚠️ Aviso: A classe {char_class.name} pode ter restrições de alinhamento.")
                        print(f"Raça {race_class.name} tende ao alinhamento: {race_instance.alignment}")
                        confirm = input("Continuar mesmo assim? (s/n): ").strip().lower()
                        if confirm != 's':
                            continue
                
                print(f"✅ Classe selecionada: {char_class.name}")
                return char_class
            else:
                print("❌ Opção inválida. Tente novamente.")

    def create_character(self, style):
        print(f"\n🎭 CRIANDO PERSONAGEM - Estilo {style.upper()}")
        
        name = input("Nome do personagem: ").strip()
        if not name:
            name = "SemNome"
        
        race_class = self.select_race()
        char_class = self.select_class(race_class)
        
        rolls = AttributeRoller.generate(style)
        print(f"\n🎲 Rolagens realizadas (6 valores):")
        for i, v in enumerate(rolls, start=1):
            print(f"  [{i}] {v}")
        
        if style == "classico":
            attributes = {ATTRIBUTE_NAMES[i]: rolls[i] for i in range(6)}
        else:
            attributes = self.distribute_attributes(rolls)
        
        character = create_character_with_race_and_class(name, style, attributes, race_class, char_class)
        
        if isinstance(char_class, Thief):
            dex_score = attributes.get("Destreza", 10)
            talents_info = char_class.initial_talents(dex_score)
            character.thief_talents = talents_info
            print(f"\n🎯 Talentos de Ladrão:")
            print(f"  Pool de pontos para distribuir: {talents_info['pool']}")
            print("  Talentos disponíveis:", ", ".join(talents_info['talents'].keys()))
        
        self.characters.append(character)
        print(f"\n✅ Personagem criado com sucesso!")
        print("\n" + "="*60)
        print(character)
        print("="*60)

    def distribute_attributes(self, rolls):
        """Permite distribuir os valores rolados nos atributos."""
        attributes = {}
        available_indices = set(range(1, 7))  # 1..6
        
        print(f"\n📊 Agora distribua os 6 valores para os atributos.")
        print("Informe o número da rolagem (1..6) que deseja atribuir a cada atributo.")
        print("Exemplo: se quiser dar o valor da rolagem [3] para Força, digite 3.")
        
        for attr in ATTRIBUTE_NAMES:
            while True:
                try:
                    print(f"\nValores disponíveis:")
                    for idx in sorted(available_indices):
                        print(f"  [{idx}] {rolls[idx-1]}")
                    
                    choice = input(f"Escolha índice para '{attr}': ").strip()
                    idx = int(choice)
                    
                    if idx < 1 or idx > 6:
                        print("❌ Índice fora do intervalo (1..6). Tente novamente.")
                        continue
                    if idx not in available_indices:
                        print("❌ Índice já usado. Escolha outro.")
                        continue
                    
                    attributes[attr] = rolls[idx-1]
                    available_indices.remove(idx)
                    print(f"✅ {attr}: {rolls[idx-1]}")
                    break
                    
                except ValueError:
                    print("❌ Entrada inválida. Digite um número inteiro (1..6).")
        
        return attributes

    def list_characters(self):
        if not self.characters:
            print("\n📝 Nenhum personagem criado ainda.")
            return
        
        print(f"\n📋 --- PERSONAGENS CRIADOS ({len(self.characters)}) ---")
        for i, character in enumerate(self.characters, start=1):
            print(f"\n[{i}] " + "="*50)
            print(character)
            
            if hasattr(character, 'thief_talents'):
                print("  🎯 Informações de Talentos:")
                talents_info = character.thief_talents
                print(f"    Pool disponível: {talents_info['pool']} pontos")
                print("    Talentos base:", ", ".join(talents_info['talents'].keys()))
            
            print("="*50)

def main():
    """Função principal do programa."""
    generator = RPGGenerator()
    generator.menu()

if __name__ == "__main__":
    main()