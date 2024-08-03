from tempfile import mkstemp
from shutil import move
from os import remove
import re
import aiofiles

'''
Image formatter

Replaces wikilinks in Obsidian with regular Markdown compliant image embeds.
This overwrites the input original file.
'''

## CSS image options tags to inline markdown image adjustments
options = {
    "-xs":"30%",
    "-s":"50%",
    "-m":"80%",
    "-l":"100%",
    "-xl":"120%",
    "-xxl":"150%",
}

expr = re.compile(r"!\[{2}[a-zA-Z0-9\-\_.\s-]+\s*\|\s*-[a-z]+\s*\|\s*-[a-z]+\]{2}")


async def replace(source_file_path):
    '''
    Given a file as specified by `source_file_path`, replace any image wikilinks to Markdown compliant links.
    Overwrites and creates a new file.
    '''
    print("Replacing wikilink in " + source_file_path)
    fh, target_file_path = mkstemp()
    async with aiofiles.open(target_file_path, "w") as target_file:
        async with aiofiles.open(source_file_path, "r") as source_file:
            async for line in source_file:
                # if line contains wikilinks, replace wikilinks
                found = expr.search(line)
                if found:
                    await target_file.write(await _replace_wikilinks(line))
                else:
                    await target_file.write(line)
    remove(source_file_path)
    move(target_file_path, source_file_path)
    return

async def _replace_wikilinks(matched_line):
    '''
    Given a line with wikilinks, replace with regular Markdown and the relevant modifiers.
    '''
    matched_line = matched_line[3:-3]
    image_args = [word.strip() for word in matched_line.split("|")]
    return await _build_string(image_args)

async def _build_string(image_args):
    img_string = image_args[0] + "|"
    for arg in image_args:
        if arg in options:
            img_string += options[arg]
    return "![[" + img_string + "]]\n"
