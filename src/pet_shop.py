# WRITE YOUR FUNCTIONS HERE

# Returns the name of the pet shop function.
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Gives the total cash of the pet shop function.
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Adds and removes cash from the pet shop function.
def add_or_remove_cash(pet_shop, cash):
    current_cash = get_total_cash(pet_shop)
    new_cash = current_cash + cash
    pet_shop["admin"]["total_cash"] = new_cash

# How many pets sold from the pet shop function.
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Increase number of pets sold from the pet shop function.
def increase_pets_sold(pet_shop, pets):
    current_pets = get_pets_sold(pet_shop)
    new_pets = current_pets + pets
    pet_shop["admin"]["pets_sold"] += pets

# Function for stock count in pet shop.

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# Function thats gets pets by breed.
def get_pets_by_breed(pet_shop, british_shorthair):
    pets_number = []
    for pet in pet_shop["pets"]:
        if pet ["breed"] == british_shorthair:
            pets_number.append(pet)
    return pets_number
