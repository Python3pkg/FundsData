import sys
import argparse

from __init__ import __version__
import funds_download
import funds_gen_sorting_files
import funds_get_top_ones


def main():
    parser = argparse.ArgumentParser(prog="python %s" % sys.argv[0])

    parser.add_argument("-d", "--download", dest='download', action='store_true',
                        help="Only download the latest web pages from http://huobijijin.com to data/webpages/<date>")

    parser.add_argument("-a", "--analyze", dest='analyze', action="store_true",
                        help="Analyze the downloaded web pages and generate the files containing sorted funds. "
                             "These files locate at data/result/<sorting_<date>")

    parser.add_argument("-r", "--run", dest='run', action='store_true',
                        help="Dry run, including download the web pages, do analysis, "
                             "and generate the top 100 and top 50 funds matching all kinds of orders. "
                             "If don't specify any option, the effect is the same as specifying this option.")

    parser.add_argument("-v", "--version", dest='version', action='store_true',
                        help="Show the version")

    args = parser.parse_args()

    if args.version:
        print "version %s" % __version__
        exit(0)

    if args.run or len(sys.argv) == 1:
        funds_download.main()
        funds_gen_sorting_files.main()
        funds_get_top_ones.main()
        exit(0)

    if args.download:
        funds_download.download_all_webpages()

    if args.analyze:
        funds_gen_sorting_files.main()


if __name__ == "__main__":
    main()
