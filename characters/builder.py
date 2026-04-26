from __future__ import annotations
import json
import os
from dataclasses import dataclass, field
from typing import Optional

from .warrior import Warrior
from .mage import Mage
from .rogue import Rogue
from .base_character import BaseCharacter
from items.equipment import Equipment
from items.factory import create_item


@dataclass(frozen=True)
class CharacterConfigs:
    """
    Immutable  configuration for building character.
    Use dataclasses.replace() to create modified copies.
    """
    name: str
    class_type: str

    # Core stats
    level: int = 1
    max_hp: int = 100
    attack: int = 10
    defense: int = 5
    speed: int = 5

    # Probability stats
    crit_chance: float = 0.10
    crit_multiplier: float = 1.5
    dodge_chance: float = 0.05

    # Class specific
    mana:  int = 0
    spell_power: int = 0
    rage: int = 0

    # Equipment keys
    weapon: Optional[str] = None
    clothes: Optional[str] = None
    armament: Optional[str] = None

    # Progression
    known_spells: tuple = field(default_factory=tuple)
    titles: tuple = field(default_factory=tuple)



class CharacterBuilder:
    """
    Build BaseCharacter instance from configs,
    JSON files, dicts, or named presets.
    """
    # registry of class type -> class
    _CLASS_MAP = {
        "warrior": Warrior,
        "mage": Mage,
        "rogue": Rogue,
    }

    _BASE_PATH: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs")

    @classmethod
    def _config_path(cls, class_type: str, filename: str) -> str:
        return str(os.path.join(cls._BASE_PATH, class_type, filename))

    # -----------Builder-------------
    @classmethod
    def from_config(cls, config: CharacterConfigs) -> BaseCharacter:
        """Build BaseCharacter from CharacterConfig dataclass."""
        char_cls =cls._CLASS_MAP.get(config.class_type)
        if char_cls is None:
            raise ValueError(f"Unknown class type: {config.class_type}")

        kwargs = {
            "name": config.name,
            "level": config.level,
            "max_hp": config.max_hp,
            "attack": config.attack,
            "defense": config.defense,
            "speed": config.speed,
            "crit_chance": config.crit_chance,
            "crit_multiplier": config.crit_multiplier,
            "dodge_chance": config.dodge_chance,
        }
        if config.class_type == "warrior":
            kwargs["rage"] = config.rage
        elif config.class_type == "mage":
            kwargs["mana"] = config.mana
            kwargs["spell_power"] = config.spell_power

        character = char_cls(**kwargs)
        character.equipment = cls._build_equipment(config)
        return character

    @classmethod
    def from_dict(cls, data: dict) -> BaseCharacter:
        """
        Build BaseCharacter from dictionary.
        """
        config = cls._dict_to_config(data)
        return cls.from_config(config)

    @classmethod
    def from_json(cls, path: str ) -> BaseCharacter:
        """Build BaseCharacter from JSON file path."""
        with open(path, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)

    @classmethod
    def from_preset(cls, class_type: str, preset_name: str) -> BaseCharacter:
        """
        Build BaseCharacter from preset JSON file.
        Example: CharacterBuilder.from_preset("warrior", "guts")
        """
        path = cls._config_path(class_type, f"{preset_name}.json")
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"Preset {preset_name} not found for '{class_type}'."
                f"Expected: {path}"
            )
        return cls.from_json(path)

    @classmethod
    def from_default(cls, class_type: str, name: str, **overrides) -> BaseCharacter:
        """
        Build character from class default with optional overrides.
        Example: CharacterBuilder.from_default("warrior", "Custom", attack=20)

        :param class_type:
        :param name:
        :param overrides:
        :return: cls. from_dict
        """
        path = cls._config_path(class_type, "defaults.json")
        with open(path, "r") as f:
            data = json.load(f)
        data["name"] = name
        data.update(overrides)
        return cls.from_dict(data)

    @classmethod
    def _dict_to_config(cls, data: dict) -> CharacterConfigs:
        """
        Convert dictionary to a CharacterConfigs.
        :param data:
        :return:
        """
        return CharacterConfigs(
            name=data.get("name", "Unknown"),
            class_type=data["class_type"],
            level=data.get("level", 1),
            max_hp=data.get("max_hp", 100),
            attack=data.get("attack",10),
            defense=data.get("defense", 5),
            speed=data.get("speed", 5),
            crit_chance=data.get("crit_chance", 0.10),
            crit_multiplier=data.get("crit_multiplier", 1.5),
            dodge_chance=data.get("dodge_chance", 0.05),
            mana=data.get("mana", 0),
            spell_power=data.get("spell_power", 0),
            rage=data.get("rage", 0),
            weapon=data.get("weapon"),
            clothes=data.get("clothes"),
            armament=data.get("armament"),
            known_spells=tuple(data.get("known_spells", [])),
            titles=tuple(data.get("titles", [])),
        )

    @classmethod
    def _build_equipment(cls, config: CharacterConfigs) -> Equipment:
        """
        Build equipment from config item keys.
        :param config:
        :return: Equipment
        """
        return Equipment(
            weapon=create_item(config.weapon) if config.weapon else None,
            clothes=create_item(config.clothes) if config.clothes else None,
            armament=create_item(config.armament) if config.armament else None,
        )