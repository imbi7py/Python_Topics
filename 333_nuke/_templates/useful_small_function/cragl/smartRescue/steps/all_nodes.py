"""Handle all nodes in the DAG but skip all nodes of specified node classes.

Args:
    mode (str): Choose how to handle matching nodes.
        disable: Will disable nodes.
        delete: Will delete nodes.
        disconnect: Will disconnect the nodes from the stream.
    skip (list of string): List of node classes to skip processing.

___________________________________________________________________________

Examples:

Standard:
    1) Will disable all nodes.

    mode: disable
    skip: ---

    ------------------------------------------------------------------------

    2) Will delete all Nodes except of Read nodes.

    mode: delete
    skip: Read

Advanced:
    1) Will disable all nodes:

    {
        "mode": "disable"
        "skip": []
    }

    ------------------------------------------------------------------------

    2) Will delete all Nodes except of Read nodes:

    {
        "mode": "delete"
        "skip": [
            "Read"
        ]
    }

"""

# Import third-party modules
______ ?  # pylint: disable=______-error

# Import local modules
____ smartRescue.base_steps ______ NodeStep


c_ AllNodes(NodeStep):
    """Handle all nodes in the DAG."""

    ___ process
        """Handle all nodes."""
        logger.info("%s all nodes, skip node classes: %s",
                         setup["mode"], ", ".join(setup["skip"]))
        ___ node __ ?.allNodes():
            __ node.Class() __ setup["skip"]:
                continue
            handle_node(node)
