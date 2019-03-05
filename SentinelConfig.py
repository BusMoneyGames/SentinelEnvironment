import argparse
import configelper
import logging

L = logging.getLogger()


def main(raw_args=None):

    print(raw_args)
    parser = argparse.ArgumentParser(description='Runs sentinel tasks for Unreal Engine.',
                                     add_help=True,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-generate", action='store_true')
    parser.add_argument("-path", default="", help="Absolute or relative path to the config directory if other than default")

    args = parser.parse_args(raw_args)
    print(raw_args)

    if args.generate and not args.path:
        L.info("Generating default config")
        configelper.generate_default_config()

    else:
        L.info("Reading config overwrite from: %s ", args.path)
        configelper.assemble_config(args.path)


if __name__ == "__main__":
    main()
