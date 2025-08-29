# elf.py
from race_interface import Race
from typing import List, Optional

class Elf(Race):
    name = "Elfo"

    @property
    def movement(self) -> int:
        return 9

    @property
    def infravision(self) -> Optional[int]:
        return 18  # metros

    @property
    def alignment(self) -> str:
        return "Tendem à neutralidade"

    @property
    def abilities(self) -> List[str]:
        return [
            "Percepção Natural: chance de detectar portas secretas",
            "Graciosos: +1 em qualquer teste de JPD",
            "Arma Racial: +1 no dano com arcos à distância",
            "Imunidades: imune a sono e paralisia de Ghoul",
        ]
