import random

class AttributeRoller:
    """Gerador de rolagens de dados para atributos."""
    @staticmethod
    def roll_3d6():
        return sum(random.randint(1,6) for _ in range(3))

    @staticmethod
    def roll_4d6_drop_lowest():
        rolls = [random.randint(1,6) for _ in range(4)]
        return sum(rolls) - min(rolls)

    @classmethod
    def generate(cls, style: str):
        """Retorna lista de 6 valores gerados conforme 'style'."""
        rolls = []
        if style == "classico" or style == "aventureiro":
            for _ in range(6):
                rolls.append(cls.roll_3d6())
        elif style == "heroico":
            for _ in range(6):
                rolls.append(cls.roll_4d6_drop_lowest())
        else:
            raise ValueError("Estilo desconhecido")
        return rolls
