# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.  
  The game is a number guessing challenge where players attempt to guess a secret number within a specified range based on difficulty level. Players receive hints like "Too High" or "Too Low" to guide their guesses, with a limited number of attempts and a scoring system that rewards efficiency.

- [X] Detail which bugs you found.  
  The first bug was that the secret number reset on every button click, making it impossible to win consistently because the target kept changing. This occurred because Streamlit reruns the entire script on each interaction, and without persistent state, variables like the secret number were reinitialized.  
  The second bug involved incorrect hint logic, where "Too High" and "Too Low" were swapped, leading players astray and preventing logical progression toward the correct guess.

- [X] Explain what fixes you applied.  
  For the session state bug, we implemented `st.session_state` to store persistent values like the secret number, attempts, score, and history, ensuring they survive Streamlit's reruns. Initialization checks were added to set these values only on the first run, and the reset function was refactored to properly clear the state for new games.  
  For the hint logic bug, we refactored the `check_guess` function into `logic_utils.py` for better testability and fixed the comparison operators to correctly identify when a guess is higher or lower than the secret. Unit tests were added to verify the logic, and the function now handles both numeric and string inputs robustly.


## 📸 Demo

- [X] [Insert a screenshot of your fixed, winning game here]
![Alt text for screenshot](/screenshot.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
