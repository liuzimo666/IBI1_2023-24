def determine_favourite_bond(birth_year):
    bond_actors = {
        1973: "Roger Moore",
        1987: "Timothy Dalton",
        1995: "Pierce Brosnan",
        2006: "Daniel Craig"
    }
    
    # calculate the year of 18
    eighteen_year_old_year = birth_year + 18
    
    # according the year to find the character of Bond
    for year, actor in bond_actors.items():
        if eighteen_year_old_year >= year:
            favourite_bond = actor
            break
    else:
        # If no find the character, print the first character
        favourite_bond = "Roger Moore"
    
    return f"Your favourite Bond actor is {favourite_bond}."

person_birth_year = 1980  # assume the birth year is 1980
print(determine_favourite_bond(person_birth_year))