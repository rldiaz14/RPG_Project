from __future__ import annotations

ENEMY_LEVEL_ADVANTAGE = 3

def determine_turn_order(player , enemy) -> tuple:
    """
    Enemy has 3 level advantage.
    If player_level > enemy_level + advantage, player goes first.
    :param player:
    :param enemy:
    :return:
    """
    player_score = player.level
    enemy_score = enemy.level + ENEMY_LEVEL_ADVANTAGE

    if player_score > enemy_score:
        return player, enemy  # player goes first
    elif enemy_score > player_score:
        return enemy, player  # enemy goes first
    else:
        # tie - use speed as tiebreaker
        if player.speed >= enemy.speed:
            return player, enemy
        return enemy, player