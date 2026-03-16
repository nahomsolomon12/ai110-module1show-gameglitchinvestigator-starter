def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare guess to secret and return a normalized outcome string.

    The caller is responsible for rendering user-facing hint text.

    This function is intentionally simple: it converts both values to int
    when possible so that numeric comparisons behave consistently even if
    the caller passes a string. If conversion fails, fall back to Python's
    default comparison semantics.
    """
    try:
        # Most of the time we compare numbers; string input should still work.
        guess_val = int(guess)
        secret_val = int(secret)
    except Exception:
        # If either value isn't numeric (e.g., None), compare using raw values.
        guess_val = guess
        secret_val = secret

    if guess_val == secret_val:
        return "Win"
    if guess_val > secret_val:
        return "Too High"
    return "Too Low"


import random


def reset_game_state(session_state, low: int, high: int):
    """Reset session state for a new game.

    This emulates the Streamlit session state used by `app.py`.
    """

    session_state.status = "playing"
    session_state.attempts = 0
    session_state.secret = random.randint(low, high)
    session_state.history = []
    session_state.score = 0


import random


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def reset_game_state(state, low: int, high: int):
    """Reset a Streamlit-like session state object for a new game.

    This is used by the UI to restart the game without recreating the app.
    """
    state.status = "playing"
    state.attempts = 0
    state.history = []
    state.score = 0
    state.secret = random.randint(low, high)
