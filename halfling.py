# halfling.py
from race_interface import Race
from typing import List, Optional

class Halfling(Race):
    name = "Halfling"

    @property
    def movement(self) -> int:
        return 6

    @property
    def infravision(self) -> Optional[int]:
        return None

    @property
    def alignment(self) -> str:
        return "Tendem à neutralidade"

    @property
    def abilities(self) -> List[str]:
        return [
            "Furtivos: chance de se esconder (1-2 em 1d6)",
            "Destemidos: +1 em testes de JPS (força de vontade)",
            "Bons de Mira: ataques de arremesso considerados fáceis",
            "Pequenos: ataques de criaturas grandes são difíceis para acertar",
            "Restrições: uso limitado de armaduras/armas grandes",
        ]
