# Print the street number and name on one line
# the city and state on the next line
# and the zip on the last line 

def parse_address(address):
  # Separate out the street address from the rest of the address
  new_str = address.split(', ')
  street = new_str.pop(0)
  # Print the street address
  print(street)
  # Separate out the state
  remaining_address = new_str.pop()
  # Separate out the country
  new_str = remaining_address.split(' ')
  middle = ', '.join(new_str[:-1])
  # Print the state and country with a comma in between
  print(middle)
  # Separate out the zipcode
  zipcode = new_str.pop()
  # Print the zipcode
  print(zipcode)

  


## Given an address
test_1 = "123 Main St., City Anystate USA 12345"
print("Input: ", test_1)
parse_address(test_1)

test_2 = "456 Commerce St., Colorado USA 54321"
print("\nInput: ", test_2)
parse_address(test_2)