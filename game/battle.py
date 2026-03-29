from __future__ import annotations
from characters.base_character import BaseCharacter
from Enemies.enemy_character import EnemyCharacter
from Enemies.behavior import enemy_turn
from game.player_action import player_attack
from game.result import BattleResult
from game.turn_order import determine_turn_order


MAX_TURNS = 50

def battle(player: BaseCharacter, enemy: EnemyCharacter) -> BattleResult:
    turn = 0
    log = []

    while player.is_alive() and enemy.is_alive() and turn < MAX_TURNS:
        turn += 1

        first, second = determine_turn_order(player, enemy)
        out1 = _take_action(first, second)
        log.append(out1)

        if not second.is_alive():
            break

        out2 = _take_action(second, first)
        log.append(out2)
    return  _resolve(player, enemy, turn, log)


def _take_action(actor, target) -> dict:
    if isinstance(actor, EnemyCharacter):
        return enemy_turn(actor, target, getattr(actor, "spell_keys", []))
    return player_attack(actor, target)

def _resolve(player, enemy, turns, log) -> BattleResult:
    if player.is_alive() and not enemy.is_alive():
        return BattleResult(outcome="win", turns=turns,
                            xp_gained=enemy.xp_reward, log=log)
    elif not player.is_alive():
        return BattleResult(outcome="loss", turns=turns,
                            xp_gained=0, log=log)
    else:
        return BattleResult(outcome="draw", turns=turns,
                            xp_gained=0, log=log)