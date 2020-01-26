word,guess = input(),input()

chars_in_word = set(word)
max_guesses = len(chars_in_word)-1 + 10
state = 'WIN'

for char in chars_in_word:
    if guess.find(char) >= max_guesses:
      state = 'LOSE'

print(state)
