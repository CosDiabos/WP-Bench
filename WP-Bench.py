import sublime
import sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")

class create_base_pluginCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.error_message(str(self))

class create_base_themeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		console.log("LPOL")

class UnwebifyCommand(sublime_plugin.TextCommand):  #Unwebify command
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				news = s.replace('&lt;', '<')  #reversed from Webify
				news = news.replace('&gt;', '>')  #reversed from Webify
				self.view.replace(edit, region, news)

class WebifyCommand(sublime_plugin.TextCommand): #create Webify Text Command
	def run(self, edit):   #implement run method
		for region in self.view.sel():  #get user selection
			if not region.empty():  #if selection not empty then
				s = self.view.substr(region)  #assign s variable the selected region
				news = s.replace('<', '&lt;')
				news = news.replace('>', '&gt;')
				self.view.replace(edit, region, news) #replace content in view

class popupTextCommand(sublime_plugin.WindowCommand):
	def run(self):
		view.show_popup_menu(['a','b'], 'lol')

	def lol(index):
		sublime.status_message("?! " + index)


class wordOnHover(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
    	if (hover_zone == 1) :
    		sublime.status_message(view.substr(view.word(point)))