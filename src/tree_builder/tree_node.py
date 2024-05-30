import dataclasses


@dataclasses.dataclass
class TreeNode:
    name: str
    children: list["TreeNode"]
