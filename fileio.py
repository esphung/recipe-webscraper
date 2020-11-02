from pathlib import Path
import json

def readFile():
	data = {}
	if Path("data.json").is_file() != True:
		return {}

	try:
		with open('data.json', 'r') as f:
			try:
				data = json.loads(f.read())
			except:
				data['recipes'] = []
	except Exception as e:
		print("{}".format(e))
		file = "data.json" # .replace(" ","")
		f = open(file,mode="w")
		f.write("{}")
		f.write("\n")
		f.truncate()
		f.close()
	return data

def writeRecipeData(data):
	if Path("data.json").is_file() != True:
		writeNewFile()
	content = readFile()
	for item in content["recipes"]:
		if item["recipe_id"] == data["recipe_id"]:
			item = data
			with open('data.json', 'w') as outfile:
				json.dump(content, outfile, sort_keys=True, indent=2)
				return content

	content["recipes"].append(data)
	with open('data.json', 'w') as outfile:
		json.dump(content, outfile, sort_keys=True, indent=2)
		return content

def writeNewFile():
	file = "data.json"
	''' simple file writing '''
	f = open(file,mode="w")
	f.write('{ "recipes": [] }')
	f.write("\n")
	f.truncate()
	f.close()
