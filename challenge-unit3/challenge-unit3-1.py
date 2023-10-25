def linear_search_product(products, target_product):
  indices = []
  for i in range(len(products)):
      if products[i] == target_product:
          indices.append(i)
  return indices

# Example usage:
products = ["apple", "banana", "orange", "apple", "grape", "apple"]
target_product = "apple"
result = linear_search_product(products, target_product)
print(result)  # Output: [0, 3, 5]
