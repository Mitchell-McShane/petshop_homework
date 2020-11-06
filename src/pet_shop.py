# WRITE YOUR FUNCTIONS HERE

# Returns the name of the pet shop.
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Gives the total cash of the pet shop.
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Adds and removes cash in the pet shop.
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash