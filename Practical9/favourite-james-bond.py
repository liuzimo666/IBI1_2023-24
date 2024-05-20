def determine_favorite_bond(birth_year):
    bond_actors = {
        1973: 'Roger Moore',
        1987: 'Timothy Dalton',
        1995: 'Pierce Brosnan',
        2006: 'Daniel Craig'
    }
    
    # Set the year of each actor's last film, according to the time period given in the title
    last_bond_years = {
        'Roger Moore': 1986,
        'Timothy Dalton': 1994,
        'Pierce Brosnan': 2005,
        'Daniel Craig': 2021  
    }
    
    # Calculate the year the individual started watching Bond movies 
    watch_year = birth_year + 18
    
    # Iterate through the bond_actors dictionary to find the actors corresponding to the year in which you started watching
    for year, actor in bond_actors.items():
        if watch_year >= year:
            # Check to see if the year of the actor's last film is past
            if last_bond_years[actor] >= watch_year:
                return actor
            else:
                # If the actor's last film year has passed, find the next actor
                continue
    
    # If no suitable actor is found (which in theory should not happen unless a very small year has been entered), the last actor is returned
    return list(bond_actors.values())[-1]

# Example function call
print(determine_favorite_bond(1980))  