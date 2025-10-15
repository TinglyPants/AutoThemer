from lib.base_palette import BasePalette
from lib.generated_palette import GeneratedPalette
from lib.validate import validate_hex_string
import json
import sys
import os
import re
import subprocess

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
    
def save_generated_palette(generated_palette, palette_name):
    with open(f"./generated-palettes/{palette_name}.json", "w") as palette_file:
        palette_dict = {}

        palette_dict["bg-dark"] = generated_palette.bg_dark
        palette_dict["bg"] = generated_palette.bg
        palette_dict["bg-light"] = generated_palette.bg_light

        palette_dict["text"] = generated_palette.text
        palette_dict["text-muted"] = generated_palette.text_muted
        
        palette_dict["accent"] = generated_palette.accent
        palette_dict["on-accent"] = generated_palette.on_accent

        palette_dict["primary"] = generated_palette.primary
        palette_dict["on-primary"] = generated_palette.on_primary

        palette_dict["error"] = generated_palette.error
        palette_dict["warning"] = generated_palette.warning
        palette_dict["success"] = generated_palette.success
        palette_dict["info"] = generated_palette.info

        palette_json = json.dumps(palette_dict, indent=4)
        palette_file.write(palette_json)

def synchronise_palette(filename, palette_name):
    # read .base
    base_file_text = ""
    with open(f"./synchronise-palettes/{filename}.base", "r") as base_file:
        base_file_text = base_file.read()

    target_output_directory = ""
    converter = ""
    with open(f"./synchronise-palettes/{filename}.output-settings.json", "r") as output_settings_file:
        output_settings_json = json.load(output_settings_file)
        target_output_directory = output_settings_json["output"]
        converter = output_settings_json["converter"]

    palette_dict = {}
    with open(f"./generated-palettes/{palette_name}.json", "r") as palette_file:
        palette_dict = json.loads(palette_file.read())

    pattern = re.compile(r"\$AutoThemer\(.*?\)")

    def substitution(match):
        key = str(match.group(0)).removeprefix("$AutoThemer(").removesuffix(")")
        hex = palette_dict[key]
        result = subprocess.run(
            ["python", f"./palette-format-converters/{converter}", hex],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    
    result = pattern.sub(substitution, base_file_text)

    with open(f"{target_output_directory}/{filename}", "w") as output_file:
        output_file.write(result)

    

if __name__ == "__main__":
    palette_filename = sys.argv[1]
    print(palette_filename)
    if "--new" in sys.argv:
        base_palette = read_base_palette()
        generated_palette = GeneratedPalette(base_palette)
        save_generated_palette(generated_palette, palette_filename)

    synchronise_palettes_path = "./synchronise-palettes"

    for filename in os.listdir(synchronise_palettes_path):
        if filename.endswith(".base"):
            filename_without_extension = filename.rsplit('.base', 1)[0]
            synchronise_palette(filename_without_extension, palette_filename)
