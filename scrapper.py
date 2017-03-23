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

print feed[0:len(feed)]
exit()
q = open('Functions.list', 'r');
q = 'merge_filters,add_action'
q = q.split(',')
referenceURL = "https://developer.wordpress.org/reference/functions/";
funcs=[]
params = []
args = []
Targs = []
Tparams = []
Tfunc = []
print 'Wordpress Functions: \n', q

for func in q:
	page = requests.get(referenceURL + func)
	tree = html.fromstring(page.content)
	print '\nFrom page:\n' + referenceURL + func
	#Does the sumbitch exists?
	print "\nFunction:\n", func
	
	if (tree.xpath('count(//*[@id="main"]/section[@class="error-404 not-found"])') == 0):
		desc = tree.xpath('//*[@class="summary"]')[0].text_content()
		desc = " ".join(desc.split())
		argsTree = tree.xpath('//*/div/section[2]/dl/dt');
		i = 1
		Tfunc.append([func, desc])
		print "\nDescription:\n", desc
		print "\nArgs:\n"
		for argsItem in argsTree:
			Targs.append([argsItem.text])
			typeP = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p/span[1]/span')[0]
			mandatory = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p[1]/span[2]')[0]
			argDesc = tree.xpath('//*/div/section[2]/dl/dd[' + str(i) + ']/p[1]/span[3]')[0]
			print argsItem.text
			print "(" + typeP.text_content() + ") " + mandatory.text_content() + " " + " ".join(argDesc.text_content().split()) + "\n"
			Tparams.append([argsItem.text + "\n(" + typeP.text_content() + ") " + mandatory.text_content() + " " + " ".join(argDesc.text_content().split())])
			i += 1


	else:
		print "\nNot found! :(\n"
		Tfunc.append([func, "Not found! :("])
		Targs.append(["nf"])
		Tparams.append(["nf"])

	print "-------"

args.append(Targs)
params.append(Tparams)
funcs.append(Tfunc) 

argsD = open('Args.json', 'w')
argsD.write(json.dumps(args));
argsD.close();

paramsD = open('Params.json', 'w')
paramsD.write(json.dumps(params));
paramsD.close();

funcsD = open('Functions.json', 'w')
funcsD.write(json.dumps(funcs));
funcsD.close();