import argparse
from tree_builder.tree_builder import TreeBuilder


def run_repl(tree_builder: TreeBuilder) -> None:
    while True:
        try:
            mess = input()
            if mess == "tree":
                tree_builder.display_tree()
            elif mess == "quit":
                break
            elif mess == "":
                continue
            else:
                print(f"[INFO]: Incorrect command, use [tree/quit]")
        except KeyboardInterrupt:
            break


def parse_arguments() -> tuple[str, str]:
    parser = argparse.ArgumentParser(description="Zookeeper Watcher")
    parser.add_argument(
        "--node_name", type=str, help="The name of the Zookeeper node to watch"
    )
    parser.add_argument(
        "--application_path", type=str, help="The path to the application"
    )

    args = parser.parse_args()

    return args.node_name, args.application_path
