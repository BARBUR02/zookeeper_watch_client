from tree_builder.tree_builder import TreeBuilder
from zookeper_watcher.zookeper_watcher import ZookeeperWatcher
from utils import run_repl, parse_arguments


def main() -> None:
    node_name, application_path = parse_arguments()
    zkw = ZookeeperWatcher(node_name, application_path)
    tree_builder = TreeBuilder(zkw)
    zkw.start()

    print(node_name, application_path)
    run_repl(tree_builder)

    zkw.application_manager.close_app()
    zkw.stop()


if __name__ == "__main__":
    main()
