from operations.argument_parsing import *
from handlers.input_handler import handle_input


def main():
    parser = define_args()
    handle_input(parser)


if __name__ == "__main__":
    main()
