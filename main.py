def product_elements(list_numbers):

    product = 1
    for element in list_numbers:
        product *= element
    return product

def minimum_list(list_numbers):

    minimum = list_numbers[0]
    for element in list_numbers:
        if element < minimum:
            minimum = element
    return minimum

def prime_number(list_numbers):

    quantity = 0
    for element in list_numbers:
        if element <= 1:
            continue
        proste = True
        for i in range(2, int(element ** 0.5) + 1):
            if element % i == 0:
                proste = False
                break
        if proste:
            quantity += 1
    return quantity

def remove_element(list_numbers, element):

  number_removed = 0
  for i in range(len(list_numbers) - 1, -1, -1):
    if list_numbers[i] == element:
      del list_numbers[i]
      number_removed += 1
  return number_removed

def concatenate_lists(list_numbers, list_numbers_2):
  combined_list = list_numbers + list_numbers_2
  return combined_list

def raise_to_power(list_numbers, power):
  new_list = []
  for number in list_numbers:
    new_element = number ** power
    new_list.append(new_element)
  return new_list


list_numbers = [1, 2, 3, 4, 5]
list_numbers_2 = [6, 7, 8, 9, 10]
product = product_elements(list_numbers)
print(f"Product of list items: {product}")

list_minimum = minimum_list(list_numbers)
print(f"The minimum value in the list: {list_minimum}")

prime_number = prime_number(list_numbers)
print(f"Number of primes in the list: {prime_number}")

element = 2
number_removed = remove_element(list_numbers, element)
print(f"Number of elements removed: {number_removed}")
print(f"List after removal: {list_numbers}")

combined_list = concatenate_lists(list_numbers, list_numbers_2)
print(f"Combined list: {combined_list}")

power = 2
new_list = raise_to_power(list_numbers, power)
print(f"New list: {new_list}")





