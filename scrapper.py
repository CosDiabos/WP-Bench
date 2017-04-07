from lxml import html
import requests
import json

feed = ['Action-Filter-and-Plugin.log',
		'Category-Tag-and-Taxonomy.log',
		'Comment-Ping-and-Trackback.log',
		'Feed.log',
		'Formatting.log',
		'HTTP-API.log',
		'Misc.log',
		'Multisite.log',
		'Post-Custom-Post-Type-Page-Attachment-and-Bookmarks.log',
		'Theme-Related.log',
		'User-and-Author.log']

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
</snippet>
"""

#for file in feed:
#q = open('Data/' + file, 'r');
q = 'add_action'
q = q.split(',')
referenceURL = "https://developer.wordpress.org/reference/functions/";

print 'Wordpress Functions: \n', q

for func in q:
	callables = 0
	page = requests.get(referenceURL + func)
	tree = html.fromstring(page.content)
	print '\nFrom page:\n' + referenceURL + func
	#Does the sumbitch exists?
	print "\nFunction:\n", func
	base = func + "("
	description_o = ""
	if (tree.xpath('count(//*[@id="main"]/section[@class="error-404 not-found"])') == 0):
		desc = tree.xpath('//*[@class="summary"]')[0].text_content()
		desc = " ".join(desc.split())
		argsTree = tree.xpath('//*/div/section[2]/dl/dt');
		i = 1
		baseCallable = ""
		snipSnip = template
		description_o += "\nDescription:\n" + desc
		description_o += "\nArgs:\n"
		for argsItem in argsTree:
			base += "${" + str(i) + ":\\" + argsItem.text + "}, "
			typeP = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p/span[1]/span')[0]
			mandatory = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p[1]/span[2]')[0]
			argDesc = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p[1]/span[3]')[0]
			description_o += argsItem.text + "\n"
			description_o += "(" + typeP.text_content() + ") " + mandatory.text_content() + " " + " ".join(argDesc.text_content().split()) + "\n"

			if (typeP.text_content() == "callable"):
				baseCallable +=  (
								"function ${" + str(i) + ":"''"} (${" + str(i + 1) + ":#Args...}) {" 
								"	${" + str(i + 2) + ":#Code...}"
								"}")
				print baseCallable
			i += 1
		base += ");\n\n"
		base += baseCallable + "\n\n"
		snipSnip = snipSnip.replace('__content__',base)
		snipSnip = snipSnip.replace('__tabTrigger__',func)
		snipSnip = snipSnip.replace('__description__',description_o)
		argsD = open(func + '.sublime-snippet', 'w')
		argsD.write(snipSnip)
		argsD.close()
		print snipSnip
	else:
		print "\nNot found! :(\n"

	print "-------"

