from typing import Any
from tree_builder.tree_node import TreeNode
from zookeper_watcher.zookeper_watcher import ZookeeperWatcher


class TreeBuilder:
    def __init__(self, zkw: ZookeeperWatcher) -> None:
        self.zkw = zkw

    def display_tree(self) -> None:
        tree = self.zkw.get_children(self.zkw.node_name)
        if tree:
            self._print_recursive(tree)
        else:
            print(f"[INFO]: {self.zkw.node_name} doesn't currently exist")

    def _print_recursive(self, tree_node: TreeNode, depth=0) -> None:
        self._indent(depth)
        print(tree_node.name)
        for child in tree_node.children:
            self._print_recursive(child, depth + 1)

    def _indent(self, depth: int) -> str:
        indent = "".join(["| " for i in range(depth + 1)])
        print(indent, end="")
