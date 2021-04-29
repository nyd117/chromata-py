import logging
import os
import re
from typing import List

from operations import utils
from operations.color_conversions import Color
from runtime_constants import TEMPLATE_DIR, ROOT_PATH


def regex_map(colors: List[Color], lines, output_file):

    for i, line in enumerate(lines):
        for entry in re.finditer(r'(\[COLOR_([0-9]|1[0-5])])', line):
            field_id = entry.group(2)
            wrapped_color = colors[utils.wrap_integer(int(field_id), 0, 7)]
            lines[i] = lines[i].replace(entry.group(1), "\"" + str(wrapped_color) + "\"")
        for entry in re.finditer(r'(\[COLOR_(B)])', line):
            lines[i] = lines[i].replace(entry.group(1), "\"" + str(colors[0]) + "\"")
        for entry in re.finditer(r'(\[COLOR_(F)])', line):
            lines[i] = lines[i].replace(entry.group(1), "\"" + str(colors[7]) + "\"")
        for entry in re.finditer(r'(\[COLOR_(C)])', line):
            lines[i] = lines[i].replace(entry.group(1), "\"" + str(colors[2]) + "\"")
    return lines


def extract_templates(colors, template):
    if template == "all":
        for file in [*os.scandir(TEMPLATE_DIR)]:
            map_template(colors, file.name)
        return
    map_template(colors, template)


def map_template(colors, template):
    template_file = os.path.join(TEMPLATE_DIR, template)
    output_file = os.path.join(ROOT_PATH, "output", template + "OUT")

    if os.path.isfile(template_file):
        prepared_template = regex_map(colors, utils.read_file_raw(template_file), output_file)
        utils.save_file("".join(prepared_template), output_file)
        logging.info("Exported %s.", template)
    else:
        logging.warning("Template '%s' doesn't exist.", template)
