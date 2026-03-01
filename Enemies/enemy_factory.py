from __future__ import annotations
from dataclasses import dataclass
from typing import Type

from .enemy_character import EnemyCharacter
from characters.base_character import BaseCharacter


@dataclass(frozen=True)
class EnemyFactory:
    key: str
    cls: Type[BaseCharacter]
    default: dict

    def create(self, name: str | None = None, **overrides) -> EnemyCharacter:
        kwargs = {**self.default, "name": name or self.default["name"], **overrides}
        return self.cls(**kwargs)

ENEMIES: dict[str, EnemyFactory] = {
        "goblin": EnemyFactory(
            key="goblin",
            cls=EnemyCharacter,
            default={
                "name": "Goblin",
                "max_hp": 30,
                "attack": 8,
                "defense": 2,
                "speed": 7,
                "behavior": "aggressive",
                "xp_reward":5,
            },
        ),
        "troll": EnemyFactory(
            key="troll",
            cls=EnemyCharacter,
            default={
                "name": "Troll",
                "max_hp": 80,
                "attack": 14,
                "defense": 6,
                "speed": 3,
                "behavior": "aggressive",
                "xp_reward": 20,
            },
        ),
        "slime": EnemyFactory(
            key="slime",
            cls=EnemyCharacter,
            default={
                "name": "Slime",
                "max_hp": 45,
                "attack": 5,
                "defense": 8,
                "speed": 4,
                "behavior": "defensive",
                "xp_reward": 8,
            },
    ),
}

def spawn_enemy(enemy_key: str, name: str | None = None, **overrides) -> EnemyCharacter:
    try:
        factory = ENEMIES[enemy_key.lower()]
    except KeyError as e:
        valid = ", ".join(sorted(ENEMIES.keys()))
        raise ValueError(f"Unknown enemy '{enemy_key}'. Valid: {valid}") from e
    return factory.create(name=name, **overrides)

