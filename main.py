import sublime, sublime_plugin, webbrowser, re

class CodelookupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        urlPrefix = 'https://www.google.com/search?q='
        region = self.view.sel()[0]
        selectedText = self.view.substr(region)
        syntax = self.view.settings().get('syntax')
        language = re.sub('.*\/', '', syntax)
        language = re.sub('\..*', '', language)
        webbrowser.open(urlPrefix + language + ' ' + selectedText)