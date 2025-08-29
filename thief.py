# thief.py
from class_interface import CharacterClass
from typing import List, Dict

def ability_modifier_oldschool(score: int) -> int:
    """
    Mapeamento "old school" aproximado para modifiers usado no livro:
    - 3 -> -3
    - 4-5 -> -2
    - 6-8 -> -1
    - 9-12 -> 0
    - 13-15 -> +1
    - 16-17 -> +2
    - 18 -> +3
    """
    if score <= 3:
        return -3
    if score <= 5:
        return -2
    if score <= 8:
        return -1
    if score <= 12:
        return 0
    if score <= 15:
        return 1
    if score <= 17:
        return 2
    return 3

class Thief(CharacterClass):
    name = "Ladrão"

    @property
    def hit_die(self) -> int:
        return 6

    @property
    def class_abilities(self) -> List[str]:
        return [
            "Armas: apenas pequenas ou médias (armas grandes geram ataques difíceis).",
            "Armaduras: apenas leves (armaduras média/pesada e escudo limitam habilidades).",
            "Itens mágicos: restrições em cajados/varinhas; permitidos pergaminhos de proteção.",
            "1º - Ataque Furtivo: ataque furtivo causa dano multiplicado por 2 (e escala nos níveis).",
            "1º - Ouvir Ruídos / 3º / 6º / 10º (chance crescente de sucesso).",
            "Talentos: começa com talentos e pontos para distribuir (ver método inicial_talents)."
        ]

    def allowed_weapon(self, weapon_type: str) -> bool:
        t = weapon_type.lower()
        # proibimos 'grande'
        if "grande" in t:
            return False
        return True

    def allowed_armor(self, armor_material_or_type: str) -> bool:
        # apenas armaduras leves permitidas
        t = armor_material_or_type.lower()
        if "leve" in t or "leves" in t:
            return True
        return False

    def initial_talents(self, dex_score: int) -> Dict:
        """
        Retorna a estrutura inicial de talentos para um Ladrão no 1º nível.
        - Base: existe um conjunto de 5 talentos (Arm / Arrombar / Escalar / Furtividade / Punga).
        - O Ladrão começa com uma 'pool' de pontos adicionais para distribuir:
          pool_base = 2 (conforme trecho: "2 pontos adicionais para distribuir")
          pool_extra = 1 por modificador de DES (ex.: DES16 -> +2)
        Retorna dict { 'pool': X, 'talents': {nome: valor_inicial(0)} }
        """
        dex_mod = ability_modifier_oldschool(dex_score)
        pool_base = 2
        pool_extra = max(0, dex_mod)  # apenas bônus positivo
        pool_total = pool_base + pool_extra

        talents = {
            "Armadilha": 0,
            "Arrombar": 0,
            "Escalar": 0,
            "Furtividade": 0,
            "Punga": 0
        }

        return {"pool": pool_total, "talents": talents}
