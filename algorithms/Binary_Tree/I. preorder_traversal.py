# Implement an pre-order traversal without recursion

def preoder_traversal(tree):     # Time: O(n); space: O(h)
  path, result = [], []
  
  while path:
    curr = path.pop()
    if curr:
      result.append(curr.data)
      path += [curr.right, curr.left]
      
  return result
