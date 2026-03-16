from types import SimpleNamespace

from logic_utils import check_guess, reset_game_state


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_guess_too_low_with_string_values():
    # Fixes the bug where string comparison caused backward hint logic.
    # A guess lower than the secret should still return "Too Low" even when
    # numeric values are provided as strings.
    result = check_guess("40", "50")
    assert result == "Too Low"


def test_reset_game_state_resets_status_and_score_and_history():
    # Simulate a session_state object like Streamlit's
    state = SimpleNamespace(
        status="lost",
        attempts=5,
        secret=999,
        history=[1, 2, 3],
        score=123,
    )

    reset_game_state(state, low=1, high=10)

    assert state.status == "playing"
    assert state.attempts == 0
    assert state.history == []
    assert state.score == 0
    assert 1 <= state.secret <= 10
