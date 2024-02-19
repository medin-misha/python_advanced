import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(walk_log_path: str) -> BinaryTreeNode:
    import re

    tree: dict[int, BinaryTreeNode] = {}
    PATTERN: str = r"\d+"

    with open(walk_log_path) as log:
        for line in log.readlines():
            values: list[int] = list(map(int, re.findall(PATTERN, line)))
            if "INFO" in line and values[0] not in tree:
                tree[values[0]] = BinaryTreeNode(val=values[0])
            elif "left" in line:
                left = BinaryTreeNode(val=values[1])
                tree[values[1]] = left
                tree[values[0]].left = tree[values[1]]
            elif "right" in line:
                right = BinaryTreeNode(val=values[1])
                tree[values[1]] = right
                tree[values[0]].right = tree[values[1]]

    return next(iter(tree.values()))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )

    root = get_tree(7)
    walk(root)

    print(restore_tree("walk_log_4.txt"))
