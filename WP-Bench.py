import sublime
import sublime_plugin
import os.path
import xml.etree.ElementTree
import os
import webbrowser
import json

snippets_dirname = os.path.dirname(__file__) + "/Snippets"
settingsEvents = False

settings = {
	'popup_colors': '',
	'ShowOnHover': 0,
	'PluginOverwriteFiles':'',
	'ThemeOverwriteFiles':''
}

def getSettings():
	history_filename = 'WP-Bench.sublime-settings'
	history = sublime.load_settings(history_filename)
	settings['ShowOnHover'] = history.get("ShowOnHover")
	settings['popup_colors'] = history.get("popup_colors")
	settings['PluginOverwriteFiles'] = history.get("PluginOverwriteFiles")
	settings['ThemeOverwriteFiles'] = history.get("ThemeOverwriteFiles")


	global settingsEvents
	if settingsEvents == False :
		history.add_on_change('ShowOnHover', getSettings)
		settingsEvents = True


def goToDocURL(view, text):
	sublime.status_message("Opening Documentation Link...")
	webbrowser.open(text, new=0, autoraise=True)


class wordOnHover(sublime_plugin.EventListener):
	def on_hover(self, view, point, hover_zone):
		if (hover_zone == 1 & settings['ShowOnHover'] == 1) :
			args = view.substr(view.word(point))
			sublime.status_message(view.substr(view.sel()[0]))
			view.run_command('w_pb_get_doc', {'keyword':args, 'point':point})



class WPbGetDocCommand(sublime_plugin.TextCommand):
	import sys
	def run(self, edit, **args):

		func_name = args.get('keyword');
		if func_name == None:
			func_name = self.view.substr(self.view.word(self.view.sel()[0]))
			
		sublime.status_message(str(func_name))

		filename = os.path.join(snippets_dirname, str(func_name) + ".sublime-snippet")
		if (os.path.exists(filename)) :
				# GO!
				rootNode = xml.etree.ElementTree.parse(filename).getroot().find('description_html')
				desc_html = rootNode.text
				
				desc_html = desc_html.replace('__sett-att-color__', settings['popup_colors'][0]['ArgColor'])
				desc_html = desc_html.replace('__sett-footer-color__', settings['popup_colors'][0]['FooterLinkColor'])

				loc = args.get('point');
				if loc == None:
					loc = -1

				self.view.show_popup(desc_html, location=loc, max_width=400, on_navigate=lambda x: goToDocURL(self.view, x))

class ExampleCommand(sublime_plugin.TextCommand):
	import sys
	def run(self, edit, **args):
		print("this!!")
		def on_done(input_string):
			self.text = input_string

		window = self.view.window()
		window.show_input_panel("Plugin Name:", "",
								 on_done, None, None)


create_base_url = ""
create_name = ""

class CreateBasePluginCommand(sublime_plugin.WindowCommand):
	def run(self, dirs):
		
		if (dirs):
			def on_done(input_string):
				sublime.status_message("Creating Plugin: " + input_string)
				createBase("plugin",dirs[0], input_string)

			def on_cancel():
				sublime.status_message("User action cancelled.")

			self.window.show_input_panel("Plugin Name:", "",on_done,None,on_cancel)
		else:
			sublime.message_dialog("Please use this command on a selected folder")


class CreateBaseThemeCommand(sublime_plugin.WindowCommand):
	def run(self, dirs):
		
		if (dirs):
			def on_done(input_string):
				sublime.status_message("Creating Theme: " + input_string)
				createBase("theme",dirs[0], input_string)

			def on_cancel():
				sublime.status_message("User action cancelled.")

			self.window.show_input_panel("Theme Name:", "",on_done,None,on_cancel)
		else:
			sublime.message_dialog("Please use this command on a selected folder")



def createBase(type, path, name):
	global create_base_url, create_name
	create_name = name

	if type == "theme":
		base = open(os.path.dirname(__file__) + "/ThemeBase.json")

	if type == "plugin":
		base = open(os.path.dirname(__file__) + "/PluginBase.json")


	fileTree = json.load(base)
	if '%' in fileTree['name']:
		fileTree['name'] = name

	print ("WP-Bench :: Creating %s %s" % (type, name))
	print ("WP-Bench :: Base dir:", fileTree['name'])
	create_base_url = fileTree['name']
	if not (dirExists(path + '/' + fileTree['name'])):
		os.mkdir(path + '/' + fileTree['name'])

	else:
		print("WP-Bench :: Base dir already exists!")

	for childs in fileTree['children']:
		print ("WP-Bench :: Gonna parse parent children")
		parseChild(childs, path, settings['ThemeOverwriteFiles'] if type == "theme" else settings['PluginOverwriteFiles'])

		pass

	base.close()

def parseChild(el, path, override):
	global create_base_url, create_name
	print ("File Type:", el['type'])
	if (el['type'] == "directory"):
		if not (dirExists(path + '/' + create_base_url + '/' + el['path'])):
			os.mkdir(path + '/' + create_base_url + '/' + el['path'])
		else:
			print("WP-Bench :: Directory " + el['name'] + " already exists! Skipping...")

	elif (el['type'] == "file"):

		if "%" in el['path']:
			el['path'] = create_name+".php"
			el['name'] = create_name+".php"

		f = open(path + '/' + create_base_url + '/' + el['path'], "a" if override == 0 else "w")
		print("WP-Bench :: File " + el['name'] + " created!")
		f.close()

	if ('children' in el):
		print ("WP-Bench :: There are more children inside this child!")
		for z in el['children']:
			parseChild(z, path, override)
			pass
	pass

def dirExists(path):
	return os.path.exists(path)

getSettings()