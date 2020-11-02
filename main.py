# package dependencies
try:
	import urllib.request
	from bs4 import BeautifulSoup
	import json
	import uuid
except ImportError as e:
	print("Module missing: {}".format(e))
	pass # module doesn't exist, deal with it.

# local modules
from allrecipes import get_allrecipe_recipe_ingredients, get_allrecipe_recipe_instructions, get_allrecipe_recipe_categories
from fileio import readFile, writeNewFile, writeRecipeData
from console_colors import bcolors

base_url = "https://www.allrecipes.com/"

route = "recipe/" # 255989 # 25599

START_RECIPE_ID = 255500 # 255500

END_RECIPE_ID = 269730 # 255501 # 269730

def get_page_html(url_address):
	try:
		result = urllib.request.urlopen(url_address).read()
		soup = BeautifulSoup(result, "html.parser")
		# print(soup)
		return soup
	except Exception as e:
		return e

def getAllRecipeData(recipe_id):
	url = "{}{}{}".format(base_url, route, recipe_id)
	html = get_page_html(url)
	try:
		title = html.title
	except Exception as e:
		print("{}".format(e))
		return
	if type(html) != urllib.error.URLError:
		print()
		print(bcolors.OKGREEN + "{}".format(url) + bcolors.ENDC)
		print(bcolors.OKGREEN + "{}".format(title.text) + bcolors.ENDC)
		title = "{}".format(title.text
			.replace("Allrecipes", "")
			.replace("|", "")
			.strip()
		)
		ingredients = []
		instructions = []
		categories = []

		ingredients = get_allrecipe_recipe_ingredients(html)
		instructions = get_allrecipe_recipe_instructions(html)
		categories = get_allrecipe_recipe_categories(html)
		recipe_data = {
			"uuid": str(uuid.uuid1()),
			"recipe_id": recipe_id,
			"title": title,
			"ingredients": json.dumps(ingredients),
			"instructions": json.dumps(instructions),
			"categories": json.dumps(categories),
		}
		# print(recipe_data)
		return recipe_data
	else:
		# do something with bad url request
		print("Error html: {}".format(html))

def debug_print_recipe(recipe):
	keys = ["recipe_id", "title", "ingredients"] # list(dict(recipe))
	for item in keys:
		print(bcolors.OKBLUE + "{}: {}".format(item, json.dumps(recipe[item], indent=4, sort_keys=True).replace("\\", "")) + bcolors.ENDC)

def main():
	print("Scraping {} recipes...".format(END_RECIPE_ID - START_RECIPE_ID))
	for i in range(START_RECIPE_ID, END_RECIPE_ID):
		recipe_id = "{}".format(i)
		print(bcolors.OKCYAN + "recipe_id: {}".format(i) + bcolors.ENDC)
		recipe_data = getAllRecipeData(recipe_id)
		debug_print_recipe(recipe_data)
		writeRecipeData(recipe_data)

if __name__ == "__main__":
	main()

# print(getAllRecipeData(255504)["ingredients"])





