# AutoThemer
Quick tool to help automatic colour palette generation and synchronisation across multiple config files. 

## Palette Generation
Palettes will be generated from a supplied JSON file, `base-palette.json`.

From there, the generated palette will be shown on screen for a preview to confirm it is sufficient. From there, it will be named and stored in `generated-palettes/` as a JSON file.

## Palette Synchronisation
Configuration files that require colour palette synchronisation will be placed in the `synchronise-palettes/` directory. Each configuration file requires a JSON file to define where it should be placed after palette synchronisation, as well as the format the colours should be converted to.

Palettes are generated using the OKLab colour space, stored in OKLCH format. Since not all configuration files will support this format by default, various converters can be placed in the `palette-format-converters/` directory, as `.py` files. These will be used to convert the OKLCH colours to any other required formats on a per-file basis.

As an example, lets say we have `UI-THEME.json` in `synchronise-palettes/UI-THEME.json`. We will also need our `synchronise-palettes/UI-THEME.json.output-settings.json` file to determine where `UI-THEME.json` should be copied to afterwards, as well as the correct `.py` file to use for OKLCH conversion. 

## Palette Format Conversion
Palette format conversion is handled with `.py` files in the `palette-format-converters/` directory. Each `.py` files needs a unique name. They should take one command line argument (the OKLCH colour) and give one string output (the newly formatted colour)

## Config File Replacement Syntax
In order for palettes to be placed into the new config files, they need to be given placeholder names and then replaced before being written. The syntax for this is very simple. As an example: `$AutoThemer(bg-light)` will be replaced with whatever the value of `bg-light` is in the chosen palette, after passing through the specified format conversion file.