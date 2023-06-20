from lxml import html
import requests
import json
import time
import sys

# feed = ['Action-Filter-and-Plugin.log',
# 		'Category-Tag-and-Taxonomy.log',
# 		'Comment-Ping-and-Trackback.log',
# 		'Feed.log',
# 		'Formatting.log',
# 		'HTTP-API.log',
# 		'Misc.log',
# 		'Multisite.log',
# 		'Post-Custom-Post-Type-Page-Attachment-and-Bookmarks.log',
# 		'Theme-Related.log',
# 		'User-and-Author.log']

feed = ['wp_all_funcs.txt']
# feed = ['test.log']

template = """
<snippet>
	<content><![CDATA[__content__]]></content>
	<!-- Optional: Tab trigger to activate the snippet -->
	<tabTrigger>__tabTrigger__</tabTrigger>
	<!-- Optional: Scope the tab trigger will be active in -->
	<scope>source.php</scope>
	<!-- Optional: Description to show in the menu -->
	<description>
	<![CDATA[__description__]]>
	</description>
	<description_html>
	<![CDATA[__description_html__]]>
	</description_html>
</snippet>
"""
snippet_folder = os.path.dirname(__file__) + "/Snippets/"

#for file in feed:
q = open('Data/' + feed[0], 'r');
# q = 'add_action'
q = q.read();
q = q.split(',');
referenceURL = "https://developer.wordpress.org/reference/functions/";

#print 'Wordpress Functions: \n', q

for func in q:
	callables = 0
	page = requests.get(referenceURL + func)
	tree = html.fromstring(page.content)
	print '\nFrom page:\n' + referenceURL + func
	#Does the sumbitch exists?
	#print "\nFunction:\n", func

	base = func + "("
	description_o = ""
	description_html = ""
	if (tree.xpath('count(//*[@id="main"]/section[@class="error-404 not-found"])') == 0):
		desc = tree.xpath('//*[@class="summary"]')[0].text_content()
		desc = " ".join(desc.split())
		argsTree = tree.xpath('//*/div/section[2]/dl/dt');
		i = 1
		baseCallable = ""
		snipSnip = template
		description_o += desc
		description_html += "<p class='desc'>" + desc + "</p>\n"
		description_html += "\n\n------------<br>\n"
		for argsItem in argsTree:
			base += "${" + str(i) + ":\\" + argsItem.text + "}"
			if len(argsTree) != i:
				base += ", "

			typeP = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p/span[1]/span')
			if len(typeP) > 0:
				typeP = typeP[0]

				mandatory = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p[1]/span[@class="required"]')
				if len(mandatory) > 0:
					mandatory = mandatory[0];

					argDesc = tree.xpath('//*/div/section[2]/dl/dt[' + str(i) + ']')
					if len(argDesc) > 0:
						argDesc = argDesc[0];
					
					# description_o += argsItem.text + "\n"
					description_html += "<p style='color:__sett-att-color__'>" + argsItem.text + "</p>\n"
					# description_o += "(" + typeP.text_content() + ") " + mandatory.text_content() + "\n"
					description_html += "(<b>" + typeP.text_content() + "</b>) <i>" + mandatory.text_content() + "</i><br>\n\n\n"

					if (typeP.text_content() == "callable"):
						baseCallable +=  (
										"function ${" + str(i) + ":"'a'"} (${" + str(i + 11) + ":$$var=''}) {\n" 
										"	${" + str(i + 12) + ":#Code...}\n"
										"}")
				else:
					description_html += "\nNone.\n\n"
			i += 1

		base += ");\n\n"
		base += baseCallable + "\n\n"
		description_html += "\n\n<br><br>------------<br><br>\n"
		returnData = tree.xpath('//*/div/section[3]/p[2]')
		if len(returnData) > 0:
			returnData = returnData[0];

		description_html += "\n\nReturns: <br>\n" + returnData.text_content() + "\n"

		description_html += "\n\n <p class='footer'><a style='color:__sett-footer-color__' href='" + referenceURL + func + "'/>See online</a></p>"
		snipSnip = snipSnip.replace('__content__',base)
		snipSnip = snipSnip.replace('__tabTrigger__',func)
		snipSnip = snipSnip.replace('__description__',description_o)
		snipSnip = snipSnip.replace('__description_html__',description_html)
		argsD = open(snippet_folder + func + '.sublime-snippet', 'w')
		snipSnip = snipSnip.encode("utf8")
		argsD.write(snipSnip)
		argsD.close()
		#print snipSnip
		print "Finished... Moving on."
	else:
		print "\nNot found! :(\n"

	print "-------"
	print "Sleeping 2 secs... Brb!"
	time.sleep(2);


