ATTRIBUTE_NAMES = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

class Character:
    """Representa um personagem com nome, estilo e atributos."""
    def __init__(self, name: str, style: str, attributes: dict):
        self.name = name
        self.style = style
        self.attributes = attributes  

    def __str__(self):
        lines = [f"Nome: {self.name}  |  Estilo: {self.style.capitalize()}"]
        for attr in ATTRIBUTE_NAMES:
            lines.append(f"  {attr:13}: {self.attributes.get(attr, '-')}")
        return "\n".join(lines)
