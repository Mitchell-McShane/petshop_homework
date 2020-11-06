# WRITE YOUR FUNCTIONS HERE

# Returns the name of the pet shop function.
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Gives the total cash of the pet shop function.
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Adds and removes cash from the pet shop function.
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# How many pets sold from the pet shop function.
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Increase number of pets sold from the pet shop function.
def increase_pets_sold(pet_shop, pets):
    pet_shop["admin"]["pets_sold"] += pets
