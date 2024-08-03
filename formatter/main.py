import asyncio
import sys
from image_formatter import replace
from md_collector import get_mds

global rel_path

async def main():
    md_files = get_mds(rel_path)
    await asyncio.gather(*map(replace, md_files))

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print("Invalid usage.\nSpecify path to the markdown files.\nUsage: `python3 [dir to markdown files]`")
        sys.exit(1)
    rel_path = sys.argv[1]
    asyncio.run(main())
    