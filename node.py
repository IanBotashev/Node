import runpy
import os


class NodeNotFound(Exception):
    pass


class NodeAlreadyExists(Exception):
    pass


class Node:
    def __init__(self):
        self.nodes = {}

    def create_node(self, name, path):
        """
        Creates a node
        :param name: The name for the node
        :param path: The path to the file to be executed
        :return:
        """
        if self.check_node_existance(name):
            raise NodeAlreadyExists('Cannot create a node, because this node already exists: {}'.format(name))

        else:
            self.nodes.update({name: {"path": path}})

    def edit_node_name(self, node, new_node):
        """
        Edits the name of a node
        :param node: The node to edit.
        :param new_node: The name to rename the node to.
        :return:
        """
        if self.check_node_existance(node):
            self.nodes[new_node] = self.nodes[node]
            del self.nodes[node]

        else:
            raise NodeNotFound('No node under name "{0}" found.'.format(node))

    def edit_node_path(self, node, new_path):
        """
        Edits a nodes' path.
        :param node: The node to edit
        :param new_path: The new path to be assigned to the edit
        :return:
        """

        if self.check_node_existance(node):
            self.nodes[node]['path'] = new_path

        else:
            raise NodeNotFound('No node under name "{0}" found.'.format(node))

    def remove_node(self, node):
        """
        Remove a node
        :param node: The node to remove
        :return:
        """

        if self.check_node_existance(node):
            self.nodes.pop(node)

        else:
            raise NodeNotFound('No node under name "{0}" found.'.format(node))

    def check_node_existance(self, node):
        """
        Checks if a node exists
        :param node: The node
        :return:
        """
        for item in self.nodes:
            if item == node:
                return True

        # else
        return False

    def pull_node(self, node):
        """
        Pulls node information
        :param node: The node
        :return:
        """
        if self.check_node_existance(node):
            return self.nodes[node]

        else:
            raise NodeNotFound('No node under name "{0}" found.'.format(node))

    def run_node(self, node):
        """
        Runs a nodes path.
        :param node: The node
        :return:
        """
        if self.check_node_existance(node):
            runpy.run_path(self.nodes[node]['path'])

        else:
            raise NodeNotFound('No node under name "{0}" found.'.format(node))

    def pull_all_nodes(self):
        """
        Gets all the available nodes
        :return:
        """
        result = []
        for node in self.nodes:
            result.append(node)

        return result

    def parse_directory(self, path, skip_dirs=True):
        """
        Parses a directory, which automatically adds all the files inside as nodes. Does not turn sub-directories into nodes,
        unless skip_dirs is set to False.
        :param path: The path to the folder
        :param skip_folders: Tells node if to parse sub directories
        :return:
        """
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:

                if os.path.isfile("{0}\\{1}".format(path, file)):
                    self.nodes.update({file.split('.')[0]: {"path": "{0}\\{1}".format(path, file)}})

                elif skip_dirs is False:
                    self.parse_directory("{0}\\{1}".format(path, file), skip_dirs=False)

        else:
            raise NotADirectoryError('Path given is not a folder or does not exist: {}'.format(path))
