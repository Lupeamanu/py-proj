import argparse


def namespace():
    parser = argparse.ArgumentParser(description="Create a new python project.")

    parser.add_argument("name")
    parser.add_argument("-V", "--version")

    parsed = parser.parse_args()

    return parsed
