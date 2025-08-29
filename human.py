# human.py
from race_interface import Race
from typing import List, Optional

class Human(Race):
    name = "Humano"

    @property
    def movement(self) -> int:
        return 9  # metros

    @property
    def infravision(self) -> Optional[int]:
        return None

    @property
    def alignment(self) -> str:
        return "Qualquer um"

    @property
    def abilities(self) -> List[str]:
        return [
            "Aprendizado: +10% XP recebido",
            "Adaptabilidade: +1 em uma JP à escolha",
        ]
