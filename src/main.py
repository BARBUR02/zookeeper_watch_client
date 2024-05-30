from tree_builder.tree_builder import TreeBuilder
from zookeper_watcher.zookeper_watcher import ZookeeperWatcher


def main() -> None:
    zkw = ZookeeperWatcher(
        "/a", "/Applications/Whiteboard.app/Contents/MacOS/Whiteboard"
    )
    tree_builder = TreeBuilder(zkw)
    zkw.start()
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

    zkw.application_manager.close_app()
    zkw.stop()


if __name__ == "__main__":
    main()
