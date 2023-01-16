print("My kitty cat likes %s,\nMy kitty cat likes %s,\nMy kitty cat fell on his %s\nAnd now thinks he's a %s." % ('roast beef', 'ham', 'head', 'clam'))

questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]
print(f'Q:{questions[0]}')
print(f'A:{answers[0]}')
print(f'Q:{questions[1]}')
print(f'A:{answers[1]}')
print(f'Q:{questions[2]}')
print(f'A:{answers[2]}')

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

song_list = song.split()
print(song_list)
song_list[14] = song_list[14].title()
song_string = ' '.join(song_list)
print(song_string)

#idx = song.rfind('m')
#song = song.replace(song[idx], song[idx].upper())
#print(song.endswith('moray!'))
