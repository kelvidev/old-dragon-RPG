# dwarf.py
from race_interface import Race
from typing import List, Optional

class Dwarf(Race):
    name = "Anão"

    @property
    def movement(self) -> int:
        return 6

    @property
    def infravision(self) -> Optional[int]:
        return 18

    @property
    def alignment(self) -> str:
        return "Tendem à ordem"

    @property
    def abilities(self) -> List[str]:
        return [
            "Mineradores: detectar anomalias em pedras (passivo)",
            "Vigoroso: +1 em testes de JPC (constituição/resistência)",
            "Armas grandes: restrições (arma grande considerada média)",
            "Inimigos: ataques contra orcs/ogros/hobgoblins considerados fáceis",
        ]
