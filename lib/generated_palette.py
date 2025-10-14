from coloraide import Color

class GeneratedPalette:
    def __init__(self, base_palette):

        self.base_palette = base_palette

        # Background
        self.bg_dark = ""
        self.bg = ""
        self.bg_light = ""
        self.generate_bg()

        # Text
        self.text = ""
        self.text_muted = ""
        self.generate_text()

        # Accent
        self.accent = ""
        self.on_accent = ""
        self.generate_accent()

        # Primary
        self.primary = ""
        self.on_primary = ""
        self.generate_primary()

    def generate_bg(self):
        bg_oklch = Color(self.base_palette.background_colour).convert("oklch")

        if self.base_palette.theme == "dark":
            bg_oklch["l"] = 0.3
        if self.base_palette.theme == "light":
            bg_oklch["l"] = 0.8

        self.bg_dark = bg_oklch.convert("srgb").to_string(hex=True)

        bg_oklch['l'] += 0.05
        self.bg = bg_oklch.convert("srgb").to_string(hex=True)

        bg_oklch['l'] += 0.05
        self.bg_light = bg_oklch.convert("srgb").to_string(hex=True)

    def generate_text(self):
        if self.base_palette.theme == "dark":
            self.text = "#f2f2f2"
            self.text_muted = "#b3b3b3"

        if self.base_palette.theme == "light":
            self.text = "#0d0d0d"
            self.text_muted = "#4d4d4d"

    def generate_primary(self):
        if self.base_palette.theme == "light":
            # on-primary should be darker
            primary_oklch = Color(self.base_palette.primary).convert("oklch")

            if primary_oklch["l"] > 0.5:
                self.primary = primary_oklch.convert("srgb").to_string(hex=True)
                primary_oklch["l"] -= 0.4
                self.on_primary = primary_oklch.convert("srgb").to_string(hex=True)
            else:
                self.on_primary = primary_oklch.convert("srgb").to_string(hex=True)
                primary_oklch["l"] += 0.4
                self.primary = primary_oklch.convert("srgb").to_string(hex=True)

        if self.base_palette.theme == "dark":
            # on-primary should be lighter
            primary_oklch = Color(self.base_palette.primary).convert("oklch")

            if primary_oklch["l"] > 0.5:
                self.on_primary = primary_oklch.convert("srgb").to_string(hex=True)
                primary_oklch["l"] -= 0.4
                self.primary = primary_oklch.convert("srgb").to_string(hex=True)
            else:
                self.primary = primary_oklch.convert("srgb").to_string(hex=True)
                primary_oklch["l"] += 0.4
                self.on_primary = primary_oklch.convert("srgb").to_string(hex=True)

    def generate_accent(self):
        if self.base_palette.theme == "light":
            # on-accent should be darker
            accent_oklch = Color(self.base_palette.accent).convert("oklch")

            if accent_oklch["l"] > 0.5:
                self.accent = accent_oklch.convert("srgb").to_string(hex=True)
                accent_oklch["l"] -= 0.4
                self.on_accent = accent_oklch.convert("srgb").to_string(hex=True)
            else:
                self.on_accent = accent_oklch.convert("srgb").to_string(hex=True)
                accent_oklch["l"] += 0.4
                self.accent = accent_oklch.convert("srgb").to_string(hex=True)

        if self.base_palette.theme == "dark":
            # on-accent should be lighter
            accent_oklch = Color(self.base_palette.accent).convert("oklch")

            if accent_oklch["l"] > 0.5:
                self.on_accent = accent_oklch.convert("srgb").to_string(hex=True)
                accent_oklch["l"] -= 0.4
                self.accent = accent_oklch.convert("srgb").to_string(hex=True)
            else:
                self.accent = accent_oklch.convert("srgb").to_string(hex=True)
                accent_oklch["l"] += 0.4
                self.on_accent = accent_oklch.convert("srgb").to_string(hex=True)


