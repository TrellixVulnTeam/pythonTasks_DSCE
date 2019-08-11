from tennis import tennis_score
import pytest


examples = (("expected_score", "player1_points", "player2_points"),
                         [("Love-All",  0,  0),
                          ("Fifteen-All",   1,  1),
                          ("Thirty-All",    2,  2),
                          ])


@pytest.mark.parametrize(*examples)
def test_early_game_scores_equal(expected_score, player1_points, player2_points):
    assert expected_score == tennis_score(player1_points, player2_points)


def test_early_game_scores_equal_ordinary():
    assert "Love-All" == tennis_score(0, 0)
    assert "Fifteen-All" == tennis_score(1, 1)
    assert "Thirty-All" == tennis_score(2, 2)