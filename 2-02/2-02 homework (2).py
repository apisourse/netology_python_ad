import json
import wikipedia
import hashlib


class ChangeCase:
	def __init__(self):
		with open('countries.json', encoding='utf-8') as datafile_load:
			json_data = json.load(datafile_load)
		self.json_data = json_data
		self.start = -1
		self.file_for_write = 'export.txt'

	def __iter__(self):
		return self

	def __next__(self):
		wikipedia.set_lang("en")
		self.start += 1
		if self.start != 10:  # len(self.json_data)
			self.state = self.json_data[self.start]['name']['common']
			self.search = wikipedia.page(self.state)
			with open(self.file_for_write, 'a', encoding='utf-8') as f:
				f.writelines('{s} - {u}\n'.format(s=self.state, u=self.search.url))
			return '{s} - {u}'.format(s=self.state, u=self.search.url)
		else:
			raise StopIteration


def get_md5(file_name):
	f = open(file_name, 'r')
	for line in f:
		export = hashlib.md5(bytes(line, 'utf-8')).hexdigest()
		yield export


if __name__ == "__main__":
	for i in ChangeCase():
		pass
	for md5 in get_md5('export.txt'):
		print(md5)

print(get_md5.__name__)