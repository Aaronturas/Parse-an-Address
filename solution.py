# Print the street number and name on one line
# the city and state on the next line
# and the zip on the last line 

def parse_address(address):
  # Separate out the street address from the rest of the address
  address_parts  = address.split(", ")
  street_address = address_parts.pop(0)
  # Print the street address
  print(street_address)
  # Separate out the state 
  # Separate out the country
  remaining_address = address_parts.pop()
  address_parts = remaining_address.split(" ")
  # Print the state and country with a comma in between
  middle_line = ", ".join(address_parts)
  print(middle_line)
  # Separate out the zipcode
  zipcode = address_parts.pop()
  # Print the zipcode
  print(zipcode)


## Given an address
test_1 = "123 Main St., City Anystate USA 12345"
print("Input: ", test_1)
parse_address(test_1)

test_2 = "456 Commerce St., Colorado USA 54321"
print("\nInput: ", test_2)
parse_address(test_2)