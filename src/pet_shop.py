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

# Function that gets pets by breed.
def get_pets_by_breed(pet_shop, pet_breed):
    pets_number = []
    for pet in pet_shop["pets"]:
        if pet ["breed"] == pet_breed:
            pets_number.append(pet)
    return pets_number

# Function that gets pets by name.
def find_pet_by_name(pet_shop, pet_name):
    pets_name = None
    for pet in pet_shop["pets"]:
        if pet ["name"] == pet_name:
            pets_name = pet
    return pets_name

# Function that removes pets by name.
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet ["name"] == pet_name:
            pet_shop["pets"].remove(pet)
            break

# Function that adds pet to stock.
def add_pet_to_stock(pets_shop, pets):
    pets_shop["pets"].append(pets)

# Function thats gets customers cash.
def get_customer_cash(customers):
    return customers["cash"]

# Function that removes customers cash.
def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

# Function that gets customers pet count.
def get_customer_pet_count(customers):
    return len(customers["pets"])

# Function that adds pet to customers.
def add_pet_to_customer(pets_shop, customers):
    pets_shop["pets"].append(customers)