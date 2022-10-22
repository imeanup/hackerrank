# Compute the right sibling tree

def construct_right_sibling(tree):   # Time: O(n), Space: O(1)
  
  def populate_children_next_field(start_node):
    while start_node and start_node.left:
#       Populate left child's next field.
      start_node.left.next = start_node.right
#       Populate right child's next field if iter is not the last node of level.
      start_node.right.next = start_node.next and start_node.next.left
      start_node = start_node.next
      
    while tree and tree.left:
      populate_children_next_field(tree)
      tree = tree.left
