class BasePalette:
    def __init__ (self, theme, background_style, accent, primary):
        self.theme = theme
        self.background_style = background_style
        self.accent = accent
        self.primary = primary

        # Default Values
        self.error = "#cc6566"
        self.warning = "#cccc65"
        self.success = "#65cc64"
        self.info = "#8c8cd9"

        self.background_colour = "#000000"

    def configure_error(self, error):
        self.error = error

    def configure_warning(self, warning):
        self.warning = warning

    def configure_success(self, success):
        self.success = success

    def configure_info(self, info):
        self.info = info

    def configure_background_colour(self, background_colour):
        self.background_colour = background_colour