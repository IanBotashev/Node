# Node
A simple command manager, which uses "nodes" for command creation and management.  
Was made for personal use.

Python Version: 3.7

## How it works?
Node works by, creating a key inside a dictionary, naming it whatever the user wants and assigning a path to it, which then call be run, with only the name of the node.

### Example
Imagine we have a node named "test", with a path to a file assigned to it, for example "commands/test.py". Once node "test" is called, it will run "commands/test.py"

## Use
- create_node(name, path)  
  Creates a node. Assigns the path to the name, and then puts it into the dictionary "nodes"
  - name  
  The name for the node to be assigned.
  - path  
  The path for the node to be assigned as
  
- remove_node(node)  
  Removes a node, permanent, and cannot be reversed, unless added back in manually.
  - node  
  The node to remove.  
  
- pull_node(node)  
  Returns information about a node, which currently is only the path of the node.
  - node  
  The node to pull information from.

- run_node(node)  
  Runs a nodes path.
  - node  
  The node to run.

- parse_directory(path, skip_dirs)  
  Parses a directory, which turns every files inside into a node. It parses every file by it's name. It does not parse sub-directories. 
  If you want for it to parse sub-directories, set "skip-dirs" to "False"  
  - path  
  The path to the directory to parse.
  - skip-dirs  
  Tells node, if to skip sub-directories. By default is set to "True"
  
- pull_all_nodes()  
  Pulls all nodes names. If you want to get all the nodes information, call the variable "nodes" instead.
 
- check_node_existance(node)  
   Checks if a node exists.
   - node  
   Checks if this node exists.

- edit_node_name(node, new_node)  
  Edits a nodes name.
  - node  
  The old node to edit
  - new_node
  The new node name.

- edit_node_path(node, new_path)
  Edits a nodes path.
  - node
  The node to edit
  - new_path
  The new path to assign to the node
  
  
