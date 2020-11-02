def get_allrecipe_recipe_ingredients(html):
	ingredients = []
	try:
		input_tag = html.find(attrs={"class" : "keyvals"})
		keys = list(input_tag.attrs.keys())
		# print(keys)
		for value in range(0, len(keys)):
			if "ingredients" in keys[value]:
				raw_string_ingredients = input_tag.attrs[keys[value]]
				ingredients = raw_string_ingredients.split()
				return ingredients
	except Exception as e:
		# print("{}".format(e))
		return []
	return ingredients

def get_allrecipe_recipe_categories(html):
	categories = []
	try:
		input_tag = html.find(attrs={"class" : "keyvals"})
		keys = list(input_tag.attrs.keys())
		# print(keys)
		for value in range(0, len(keys)):
			if "categories" in keys[value]:
				# print(input_tag.attrs[keys[value]].split("/"))
				arr = input_tag.attrs[keys[value]].split("/")
				arr.remove("")
				for i in range(0, len(arr)):
					if "|" in arr[i]:
						arr[i] = arr[i].replace("|", "")
				categories = list(dict.fromkeys(arr))
		return categories
	except Exception as e:
		# print("{}".format(e))
		return []
	print(categories)
	return categories
def get_allrecipe_recipe_instructions(html):
	instructions = []
	try:
		input_tag = html.find(attrs={"class" : "instructions-section"})
		elements = input_tag.findAll(attrs={"class", "paragraph"})
		for i in range(0, len(elements)):
			instructions.append(elements[i].p.text)
			# print(elements[i].p.text)
		# print(keys)
		# for value in range(0, len(keys)):
		# 	if "instructions" in keys[value]:
		# 		print(keys[value])
	except Exception as e:
		print("{}".format(e))
	# print(instructions)
	return instructions