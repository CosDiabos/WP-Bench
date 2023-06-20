#!/usr/bin/python

from lxml import html
import requests
import json
import time


max_pages = 50
curr_page = 1
lists = []
debug = True
funcs = ""

while curr_page <= max_pages:
	if (curr_page == 1):
		referenceURL = "https://developer.wordpress.org/reference/functions/";
		if debug == True:
			print ("Fetching page 1...")

	else:
		referenceURL = "https://developer.wordpress.org/reference/functions/page/" + str(curr_page);
		if debug == True:
			print ("Fetching page " + str(curr_page) +  "...")


	page = requests.get(referenceURL)
	tree = html.fromstring(page.content)
	l = tree.xpath('//article[contains(@class,"-function")]/h1/a')
	if debug == True:
		print ("Items retrieved, appending...")
		#print (l)
		#print ("Appending...")
	
	lists.append(l);
	curr_page += 1
	if debug == True:
		print ("Sleeping 1 sec... Brb!")
	
	time.sleep(1);

for list_item in lists:
	for func_name in list_item:
		funcs += func_name.text_content() + ","

file = open("wp_all_funcs.txt", "w")
if debug == True:
	print ("Writing output file...")

file.write(funcs)
file.close()

# for func in q:
# 	callables = 0
# 	page = requests.get(referenceURL + func)
# 	tree = html.fromstring(page.content)
# 	print ('\nFrom page:\n' + referenceURL + func)
# 	#Does the sumbitch exists?
# 	print ("\nFunction:\n", func)
# 	base = func + "("
# 	description_o = ""
# 	if (tree.xpath('count(//*[@id="main"]/section[@class="error-404 not-found"])') == 0):
# 		desc = tree.xpath('//*[@class="summary"]')[0].text_content()
# 		desc = " ".join(desc.split())
# 		argsTree = tree.xpath('//*/div/section[2]/dl/dt');
# 		i = 1
# 		baseCallable = ""
# 		snipSnip = template
# 		description_o += "\nDescription:\n" + desc
# 		description_o += "\nArgs:\n"
# 		for argsItem in argsTree:
# 			base += "${" + str(i) + ":\\" + argsItem.text + "}, "
# 			typeP = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p/span[1]/span')[0]
# 			mandatory = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p[1]/span[2]')[0]
# 			argDesc = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p[1]/span[3]')[0]
# 			description_o += argsItem.text + "\n"
# 			description_o += "(" + typeP.text_content() + ") " + mandatory.text_content() + " " + " ".join(argDesc.text_content().split()) + "\n"

# 			if (typeP.text_content() == "callable"):
# 				baseCallable +=  (
# 								"function ${" + str(i) + ":"''"} (${" + str(i + 1) + ":#Args...}) {" 
# 								"	${" + str(i + 2) + ":#Code...}"
# 								"}")
# 				print (baseCallable)
# 			i += 1
# 		base += ");\n\n"
# 		base += baseCallable + "\n\n"
# 		snipSnip = snipSnip.replace('__content__',base)
# 		snipSnip = snipSnip.replace('__tabTrigger__',func)
# 		snipSnip = snipSnip.replace('__description__',description_o)
# 		argsD = open(func + '.sublime-snippet', 'w')
# 		argsD.write(snipSnip)
# 		argsD.close()
# 		print (snipSnip)
# 	else:
# 		print ("\nNot found! :(\n")

# 	print ("-------")

