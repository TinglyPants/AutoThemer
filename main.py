from lib.base_palette import BasePalette
from lib.generated_palette import GeneratedPalette
from lib.validate import validate_hex_string
import json
import sys

def read_base_palette():
    # Read base-palette.json and return a BasePalette
    with open("base-palette.json", "r") as file:
        base = json.load(file)

        # Ensure required properties
        required_properties = ["theme", "background-style", "accent", "primary"]
        for required_property in required_properties:
            if not required_property in base:
                print(f"Missing required entry: {required_property}")
                sys.exit()

        # Load required properties
        base_palette = BasePalette(base["theme"], base["background-style"], base["accent"], base["primary"])

        # Validate required properties
        if base_palette.theme == "light":
            print("Theme: light")
        elif base_palette.theme == "dark":
            print("Theme: dark")
        else:
            print(f"Invalid value for theme: {base_palette.theme}")
            sys.exit()

        if base_palette.background_style == "neutral":
            print("Background style: neutral")
        elif base_palette.background_style == "colour":
            print("Background style: colour")
            if not "background-colour" in base:
                print("Missing required entry: background-colour")
                sys.exit()
            else:
                if validate_hex_string(base["background-colour"]):
                    base_palette.configure_background_colour(base["background-colour"])
                    print(f"Background colour: {base_palette.background_colour}")
                else:
                    print(f"Invalid value for background colour: {base["background-colour"]}")
                    sys.exit()
        else:
            print(f"Invalid value for background style: {base_palette.background_style}")
            sys.exit()

        if not validate_hex_string(base_palette.accent):
            print(f"Invalid value for accent: {base_palette.accent}")
            sys.exit()
        else:
            print(f"Accent: {base_palette.accent}")

        if not validate_hex_string(base_palette.primary):
            print(f"Invalid value for primary: {base_palette.primary}")
            sys.exit()
        else:
            print(f"Primary: {base_palette.primary}")

        # Validate optional properties
        if "error" in base:
            if not validate_hex_string(base["error"]):
                print(f"Invalid value for error: {base["error"]}")
                sys.exit()
            else:
                base_palette.configure_error(base["error"])
                print(f"Error: {base_palette.error}")

        if "warning" in base:
            if not validate_hex_string(base["warning"]):
                print(f"Invalid value for warning: {base["warning"]}")
                sys.exit()
            else:
                base_palette.configure_warning(base["warning"])
                print(f"Warning: {base_palette.warning}")

        if "success" in base:
            if not validate_hex_string(base["success"]):
                print(f"Invalid value for success: {base["success"]}")
                sys.exit()
            else:
                base_palette.configure_success(base["success"])
                print(f"Success: {base_palette.success}")

        if "info" in base:
            if not validate_hex_string(base["info"]):
                print(f"Invalid value for info: {base["info"]}")
                sys.exit()
            else:
                base_palette.configure_info(base["info"])
                print(f"Info: {base_palette.info}")
        
        return base_palette


if __name__ == "__main__":
    base_palette = read_base_palette()
    generated_palette = GeneratedPalette(base_palette)

    
