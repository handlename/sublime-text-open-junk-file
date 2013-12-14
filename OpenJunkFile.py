import os
import datetime
import sublime
import sublime_plugin

class OpenJunkFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel(
            "OpenJunkFile:",
            self.default_filename(),
            self.open_junk_file,
            None, None)

    def settings(self):
        return sublime.load_settings("OpenJunkFile.sublime-settings")

    def open_junk_file(self, filename):
        dir_path = self.prepare_junk_dir()
        self.window.open_file(dir_path + "/" + filename)

    def prepare_junk_dir(self):
        junk_dir = os.path.expandvars(self.settings().get('junk_dir'))
        today = datetime.datetime.today()
        year = str(today.year)
        month = str(today.month)

        self.makedir(junk_dir)
        self.makedir("/".join([junk_dir, year]))
        self.makedir("/".join([junk_dir, year, month]))

        return "/".join([junk_dir, year, month])

    def makedir(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def default_filename(self):
        return datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
