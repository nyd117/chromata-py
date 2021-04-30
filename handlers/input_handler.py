import argparse
import logging
from typing import List

import operations.color_conversions
from backends.colorz import ColorZ
from backends.colorthief import ColorThiefBackend
from backends.backend import Backend
from operations import extraction
from operations.color_conversions import hex_to_rgb, Color
from gui.show_gui import show_gui
from operations.template_map import extract_templates
from operations.utils import trim, is_path_exists


def resolve_backend(b) -> Backend:
    if b == "colorThief":
        return ColorThiefBackend()
    return ColorZ()


def handle_input(parser: argparse.ArgumentParser) -> None:
    args = parser.parse_args()
    gui_enabled: bool = args.n is False
    backend: Backend = resolve_backend(args.b)
    target_colors = args.c or 8
    target_template = args.t or "all" if args.g else None
    execute_arg = (lambda arg, func: func(arg) if arg is not None else False)

    actions = {
        args.a: lambda arg: print(hex_to_rgb(arg)),
        args.e: lambda arg: extract_input(arg),
        args.f: lambda arg: extract_file(arg),
        args.p: lambda arg: extract_palette(arg)
    }

    def extract_input(arg):
        colors = extraction.extract(arg)
        show(trim(colors), "Colors from arguments")

    def extract_file(arg):
        path = arg
        if not is_path_exists(path):
            logging.warning("Provided path: `%s` does not exist.", path)
            return
        with open(path, mode='r') as file:
            lines = file.read()
        colors = extraction.extract(lines)
        show(trim(colors), "Colors from file")
        # TODO trim should be done only for operations where input has been read due to
        # TODO a path and/or argument and not during palette extraction and only after user specification

    def extract_palette(arg):
        colors = backend.get_colors(arg, target_colors)
        show(colors, "Palette")
        if args.g:  # make this separate action
            generate_templates(colors)

    def generate_templates(colors):
        extract_templates(colors, target_template)

    def show(colors: List[Color], header):
        print(header)
        colors.sort(key=lambda c: operations.color_conversions.step_inv_lum_hsv(c, len(colors)))
        colors = list(colors)
        for color in colors:
            print(color.rgb_string)
        assert_gui(colors)

    def assert_gui(col):
        if gui_enabled:
            show_gui(col)

    for argument, action in actions.items():
        execute_arg(argument, action)
