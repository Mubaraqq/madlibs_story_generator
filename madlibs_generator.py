import os

# Get the directory where your Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
story_path = os.path.join(script_dir, 'story.txt')

# read story file
with open(story_path, 'r') as f:
    story = f.read()

# defines the characters that mark the start and end of placeholders
starting_target = "<"
ending_target = ">"

# creates an empty set to store unique placeholders
words = set()

# acts as a flag or pointer to remember where a placeholder begins
# the value -1 is used because array indices start at 0, so -1 means no valid position found yet
start_of_word = -1

# loops through each character with its index
for i, char in enumerate(story):
    if char == starting_target:              # when '<' is found
        start_of_word = i                    # remember this position

    if char == ending_target and start_of_word != -1:   # when '>' is found AND we have a start position
        word = story[start_of_word: i + 1]   # extract the full placeholder
        words.add(word)                      # add to set
        start_of_word = -1                   # reset for next placeholder

# dictionary to store user responses
answers = {}

# for each placeholder, prompts user for a word
for word in words:
    answer = input(f'Enter a word for {word}: ')
    answers[word] = answer                    # stores answer in dictionary with placeholder as key

# replaces each occurrence of the placeholder with user's word
for word in words:
    story = story.replace(word, answers[word])

print(story)

