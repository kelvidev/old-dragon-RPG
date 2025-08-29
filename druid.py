from class_interface import CharacterClass
from typing import List

class Druid(CharacterClass):
    name = "Druida"

    @property
    def hit_die(self) -> int:
        return 8

    @property
    def class_abilities(self) -> List[str]:
        return [
            "Restrições: exige alinhamento neutro; NÃO pode usar armaduras/armas metálicas (perde habilidades).",
            "1º nível - Herbalismo: identificar plantas, animais e água potável.",
            "3º nível - Previdência: acampamentos montados por druida são sempre seguros.",
            "6º nível - Transformação: assumir forma de animal pequeno (até 6 DV) até 3x/dia.",
            "10º nível - Transformação Melhorada: formas até 10 DV, 3x/dia, adota habilidades especiais do animal."
        ]

    def allowed_alignment(self, alignment: str) -> bool:
        return "neutro" in alignment.lower()

    def allowed_weapon(self, weapon_type: str) -> bool:
        return "metal" not in weapon_type.lower()

    def allowed_armor(self, armor_material_or_type: str) -> bool:
        return "metal" not in armor_material_or_type.lower()
