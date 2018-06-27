import markovify

with open('data/shakespear.txt', 'r') as f:
	text = f.read()

text_model = markovify.Text(text)

for i in range(3):
	print(text_model.make_short_sentence(140))