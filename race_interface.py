# race_interface.py
from abc import ABC, abstractmethod
from typing import List, Optional

class Race(ABC):
    """Interface/ABC para Raças. Implementações devem expor propriedades."""
    name: str

    @property
    @abstractmethod
    def movement(self) -> int:
        ...

    @property
    @abstractmethod
    def infravision(self) -> Optional[int]:
        ...

    @property
    @abstractmethod
    def alignment(self) -> str:
        ...

    @property
    @abstractmethod
    def abilities(self) -> List[str]:
        ...
