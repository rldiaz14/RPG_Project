from __future__ import annotations
from characters.base_character import BaseCharacter
from Enemies.enemy_character import EnemyCharacter
from Enemies.behavior import enemy_turn
from game.player_action import player_attack, flee_action, cast_action
from game.result import BattleResult
from game.turn_order import determine_turn_order


MAX_TURNS = 50

def battle(player: BaseCharacter, enemy: EnemyCharacter,
           action_selector=None) -> BattleResult:
    turns = 0
    log = []

    while player.is_alive() and enemy.is_alive() and turns < MAX_TURNS:
        turns += 1


        first, second = determine_turn_order(player, enemy)

        # first actor's turn
        out1 = _take_action(first, second, action_selector if first is player else None)
        log.append(out1)

        # successful flee ends battle immediately
        if out1.get("type") == "flee" and out1.get("success"):
            break

        if not second.is_alive():
            break

        out2 = _take_action(second, first, action_selector if second is player else None)
        log.append(out2)

        if out2.get("type") == "flee" and out2.get("success"):
            break

    return  _resolve(player, enemy, turns, log)


def _take_action(actor, target, action_selector=None) -> dict:
    if isinstance(actor, EnemyCharacter):
        return enemy_turn(actor, target, getattr(actor, "spell_keys", []))
    if action_selector:
        return action_selector(actor, target)
    return player_attack(actor, target)

def _resolve(player, enemy, turns, log) -> BattleResult:
    # check last action for successful flee
    if log and log[-1].get("type") == "flee" and log[-1].get("success"):
        return BattleResult(outcome="flee", turns=turns,
                            xp_gained=0, log=log)
    if player.is_alive() and not enemy.is_alive():
        return BattleResult(outcome="win", turns=turns,
                            xp_gained=enemy.xp_reward, log=log)
    elif not player.is_alive():
        return BattleResult(outcome="loss", turns=turns,
                            xp_gained=0, log=log)
    else:
        return BattleResult(outcome="draw", turns=turns,
                            xp_gained=0, log=log)