from abc import ABC, abstractmethod
from typing import List

class CharacterClass(ABC):

    name: str

    @property
    @abstractmethod
    def hit_die(self) -> int:
        ...

    @property
    @abstractmethod
    def class_abilities(self) -> List[str]:
   
        ...

    def allowed_alignment(self, alignment: str) -> bool:
        return True

    def allowed_weapon(self, weapon_type: str) -> bool:
        return True

    def allowed_armor(self, armor_material_or_type: str) -> bool:
        return True
