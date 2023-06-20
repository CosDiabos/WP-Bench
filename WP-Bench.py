import sublime
import sublime_plugin
import os.path
import xml.etree.ElementTree
import os
import webbrowser

dirname = os.path.dirname(__file__)
settingsEvents = False

settings = {
	'popup_colors': '',
	'ShowOnHover': 0
}

def getSettings():
	history_filename = 'WP-Bench.sublime-settings'
	history = sublime.load_settings(history_filename)
	settings['ShowOnHover'] = history.get("ShowOnHover")
	settings['popup_colors'] = history.get("popup_colors")

	global settingsEvents
	if settingsEvents == False :
		history.add_on_change('ShowOnHover', getSettings)
		settingsEvents = True

def showPop(selff, msg):
	self.view.show_popup(selff, "a", None, -1, 400, 200)
	#sublime.View.show_popup(selff, msg, None, -1, 400, 200)

def goToDocURL(view, text):
	sublime.status_message("Opening Documentation Link...")
	webbrowser.open(text, new=0, autoraise=True)


class wordOnHover(sublime_plugin.EventListener):
	def on_hover(self, view, point, hover_zone):
		if (hover_zone == 1 & settings['ShowOnHover'] == 1) :
			args = view.substr(view.word(point))
			sublime.status_message(view.substr(view.sel()[0]))
			view.run_command('w_pb_get_doc', {'keyword':args, 'point':point})
			#sublime.status_message(view.substr(view.word(point)))
# add_action



class WPbGetDocCommand(sublime_plugin.TextCommand):
	import sys
	def run(self, edit, **args):

		func_name = args.get('keyword');
		if func_name == None:
			func_name = self.view.substr(self.view.word(self.view.sel()[0]))
			
		sublime.status_message(str(func_name))

		filename = os.path.join(dirname  + "/Snippets", str(func_name) + ".sublime-snippet")
		if (os.path.exists(filename)) :
				# GO!
				rootNode = xml.etree.ElementTree.parse(filename).getroot().find('description_html')
				desc_html = rootNode.text
				
				#sublime.save_settings(history_filename)
				desc_html = desc_html.replace('__sett-att-color__', settings['popup_colors'][0]['ArgColor'])
				desc_html = desc_html.replace('__sett-footer-color__', settings['popup_colors'][0]['FooterLinkColor'])

				#print view.filename(), rootNode
				#self.view.insert(edit, 0, rootNode.text)
				#self.view.show_popup(self, "a", None, -1, 400, 200)
				loc = args.get('point');
				if loc == None:
					loc = -1

				self.view.show_popup(desc_html, location=loc, max_width=400, on_navigate=lambda x: goToDocURL(self.view, x))

			#showPop(self, rootNode.text)



getSettings()