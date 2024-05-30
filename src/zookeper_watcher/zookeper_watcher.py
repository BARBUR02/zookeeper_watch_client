from typing import Any, Optional
from kazoo.client import KazooState, KazooClient

from application_manager import ApplicationManager
from tree_builder.tree_node import TreeNode


class ZookeeperWatcher:
    def __init__(self, node_name: str, application_path: str) -> None:
        self.zk = KazooClient(hosts="127.0.0.1:2181")
        self.node_name = node_name
        self.application_manager = ApplicationManager(application_path)

    def _init_watch_events(self) -> None:
        self.zk.add_listener(self._connection_listener)
        self.zk.DataWatch(self.node_name)(self._node_listener)
        self.zk.ChildrenWatch(self.node_name)(self._children_listener)

    def _connection_listener(self, state: KazooState) -> None:
        if state == KazooState.LOST:
            print("[CONNECTION LOST]")
        elif state == KazooState.SUSPENDED:
            print("[CONNECTION SUSPENDED]")
        else:
            print("[CONNECTED]")

    def _children_listener(self, children: list[str]) -> None:
        print(f"[INFO]: {len(children)} children: {children}")

    def _node_listener(self, data: Optional[bytes], stat: Any) -> None:
        if stat:
            print(f"[INFO]: Node {self.node_name} created")
            print(
                f"[INFO]:\n\tNode data {data if data else '[no_data]'}\n\tNode stat: {stat}"
            )
            self.application_manager.open_app()
            self.zk.ChildrenWatch(self.node_name)(self._children_listener)
        else:
            print(f"[INFO]: Node {self.node_name} deleted")
            self.application_manager.close_app()

    def get_children(self, start_node: str, path: str = "") -> TreeNode:
        new_path = path + start_node if path else start_node
        if self.zk.exists(new_path):
            children = self.zk.get_children(new_path, [])
            return TreeNode(
                name=start_node,
                children=[
                    self.get_children(child, f"{new_path}/") for child in children
                ],
            )
        return None

    def start(self) -> None:
        self.zk.start()
        self._init_watch_events()

    def stop(self) -> None:
        self.zk.stop()
        self.zk.close()
