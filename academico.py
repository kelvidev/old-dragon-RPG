# academic.py
from class_interface import CharacterClass
from typing import List

class Academic(CharacterClass):
    name = "Acadêmico"

    @property
    def hit_die(self) -> int:
        return 8

    @property
    def class_abilities(self) -> List[str]:
        return [
            "Restrições: exige alinhamento neutro; NÃO pode usar armas cortantes ou perfurantes (mantém magias como clérigo).",
            "1º nível - Conhecimento Acadêmico: identificar monstros / hábitos (1-2 em 1d6).",
            "3º nível - Decifrar Linguagens: identificar idiomas e pictogramas (chance evolutiva).",
            "6º nível - Lendas e Tradições: identificar lendas e rumores (chance maior).",
            "10º nível - Identificar Itens: observação detalhada pode revelar propósito geral de item mágico."
        ]

    def allowed_alignment(self, alignment: str) -> bool:
        return "neutro" in alignment.lower()

    def allowed_weapon(self, weapon_type: str) -> bool:
        # proíbe armas cortantes ou perfurantes
        t = weapon_type.lower()
        if "cortante" in t or "perfurante" in t or "cort" in t or "perf" in t:
            return False
        return True
