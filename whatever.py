#Implementing a linked list of 3 nodes in which the first node is linked to the second, 
#and the second is linked to the third. The third node is the terminal node and hence
#will have no link node"""
class Node:
    def __init__(self,value:int,link_node=None):
        """Initializes the structure of the Node class instances"""
        self.value=value
        self.link_node=link_node
    def get_value(self):
        """gets the value of a specific node"""
        return self.value
    def get_link_node(self):
        """gets the link node of a particular node if it has one"""
        return self.link_node
    def set_link_node(self,link_node):
        """links a node to another node"""
        self.link_node=link_node

class linked_list:
    def __init__(self, value):#a typical linked list instance will have a value serving as it's head node
        self.head_node=Node(value)
    def get_head_node(self):
        """used to get the current head_node of the linked list"""
        return self.head_node
    def insert_new_head(self, value):
        """inserts a new value as the head of the linked list"""
        new_node=Node(value)
        new_node.set_link_node(self.head_node)
        self.head_node=new_node
    def stringify_node_values(self):
        """returns all node values in the linked list as a string"""
        string=""
        current_node=self.get_head_node()
        while current_node:
            if current_node.get_value!=None:
                string+=str(current_node.get_value())+"\n"
                current_node=current_node.get_link_node()
                
        return string
link=linked_list(3)
link.insert_new_head(2)
link.insert_new_head(1)
print(link.stringify_node_values())





    
