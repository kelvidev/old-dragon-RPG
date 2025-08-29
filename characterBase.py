# character_base.py
from typing import Dict
from class_interface import CharacterClass

ATTRIBUTE_NAMES = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

class Character:
    """Base mínima do personagem. Será combinada dinamicamente com uma Race."""
    def __init__(self, name: str, style: str, attributes: Dict[str, int], char_class: CharacterClass):
        self.name = name
        self.style = style
        self.attributes = attributes
        self.char_class = char_class

    def __str__(self):
        lines = [f"Nome: {self.name}  |  Estilo: {self.style.capitalize()}  |  Classe: {self.char_class.name}  |  Raça: {getattr(self, 'name', 'Desconhecida')}"]
        # Raça expõe movement/infravision/alignment por herança
        lines.append(f"  Movimento: {self.movement}m  |  Infravision: {self.infravision or '-'}  |  Alinhamento: {self.alignment}")
        lines.append("  Habilidades raciais:")
        for a in self.abilities:
            lines.append(f"    - {a}")
        lines.append("  Atributos:")
        for attr in ATTRIBUTE_NAMES:
            lines.append(f"    {attr:12}: {self.attributes.get(attr, '-')}")
        lines.append("  Habilidades de classe:")
        for a in self.char_class.class_abilities:
            lines.append(f"    - {a}")
        return "\n".join(lines)