# phone_book = dict()  <- this is a way to create dictionaries (aka hash tables)

# useful shortcut for making dictionaries
phone_book = {}

#now we add items to the table
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book["jenny"])

# mapping a web address to an IP address is a perfect use case for a hash table, this is also called DNS resolution

# Voting example
voted = {}

voted["tom"] = "hello"

value = voted.get("tom") # returns if "tom" is in this, None if not

print(value)