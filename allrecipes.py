import re
import unicodedata
# item = item.replace(u'\u2009', ' ')
fractions = {
		u'\u2009': '',
    u'\u2189': '', # 0.0,  # ; ; 0 # No       VULGAR FRACTION ZERO THIRDS
    u'\u2152': "1/10", # 0.1,  # ; ; 1/10 # No       VULGAR FRACTION ONE TENTH
    u'\u2151': "1/9", # 0.11111111,  # ; ; 1/9 # No       VULGAR FRACTION ONE NINTH
    u'\u215B': "1/8", # 0.125,  # ; ; 1/8 # No       VULGAR FRACTION ONE EIGHTH
    u'\u2150': "1/7", # 0.14285714,  # ; ; 1/7 # No       VULGAR FRACTION ONE SEVENTH
    u'\u2159': "1/6", # 0.16666667,  # ; ; 1/6 # No       VULGAR FRACTION ONE SIXTH
    u'\u2155': "1/5", # 0.2,  # ; ; 1/5 # No       VULGAR FRACTION ONE FIFTH
    u'\u00BC': "1/4", # 0.25,  # ; ; 1/4 # No       VULGAR FRACTION ONE QUARTER
    u'\u2153': "1/3", # 0.33333333,  # ; ; 1/3 # No       VULGAR FRACTION ONE THIRD
    u'\u215C': "1/8", # 0.375,  # ; ; 3/8 # No       VULGAR FRACTION THREE EIGHTHS
    u'\u2156': "2/5", # 0.4,  # ; ; 2/5 # No       VULGAR FRACTION TWO FIFTHS
    u'\u00BD': "1/2", # 0.5,  # ; ; 1/2 # No       VULGAR FRACTION ONE HALF
    u'\u2157': "3/5", # 0.6,  # ; ; 3/5 # No       VULGAR FRACTION THREE FIFTHS
    u'\u215D': "5/8", # 0.625,  # ; ; 5/8 # No       VULGAR FRACTION FIVE EIGHTHS
    u'\u2154': "2/3", # 0.66666667,  # ; ; 2/3 # No       VULGAR FRACTION TWO THIRDS
    u'\u00BE': "3/4", # 0.75,  # ; ; 3/4 # No       VULGAR FRACTION THREE QUARTERS
    u'\u2158': "4/5", # 0.8,  # ; ; 4/5 # No       VULGAR FRACTION FOUR FIFTHS
    u'\u215A': "5/6", # 0.83333333,  # ; ; 5/6 # No       VULGAR FRACTION FIVE SIXTHS
    u'\u215E': "7/8", # 0.875,  # ; ; 7/8 # No       VULGAR FRACTION SEVEN EIGHTHS
}
def get_recipe_image(html):
	# image-container
	image = ""
	try:
		input_tag = html.find(attrs={"class" : "image-container"})
		image_element = input_tag.img
		if image_element.attrs["alt"]:
			alt = image_element.attrs["alt"].strip().lower()
			title = html.title.text.replace("|", "").replace("Allrecipes", "").strip().lower()
			if alt in title:
				image  = image_element.attrs["src"]
	except Exception as e:
		print("{}".format(e))
	# print(image)
	return image

def get_allrecipe_recipe_ingredients(html):
	# ingredients-section
	# print(html)
	ingredients = []
	try:
		# return ingredients
		input_tag = html.find(attrs={"class" : "ingredients-section"})
		elements = input_tag.findAll(attrs={"class", "ingredients-item-name"})
		for item in elements:
			item = item.text.strip()
			for key in fractions:
				item = item.replace(key, " {}".format(fractions[key])).replace("  ", " ")
			# ingredients.append(item.replace("½", "1/2").replace("⅓", "1/3").replace("¼", "1/4").replace("⅛", "1/8").replace("⅔", "2/3").replace("¾", "3/4"))
			ingredients.append(item)
	except Exception as e:
		print("{}".format(e))
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
