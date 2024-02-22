# Author Jose Tellez

sports_leagues = {"NFL": "National Futball League (NFL)",
                  "MLP": "Major League Baseball (Baseball)",
                  "NBA": "National Basketball Association (Basketball)",
                  "EPL": "Premier League (Association Football)",
                  "NHL": "National Hockey League (Ice Hockey)",
                  "MLS": "Major League Soccer (Association football)",
                  "IPL": "Indian Premier League (Tweanty20 cricket)",
                  "AFL": "Australian Football League (Australian rules football)",
                  "NRL": "National Rugby League (Rugby League Football)",
                  "CFL": "Canadian Football League (Canadian football)"}


def delete_league():
    """
    Deletes a league in the sports_league dictionary , according to a key given by the  user. If the key does not exist
    the program prints an error message
    :return:None
    """
    global sports_leagues
    user_input = input("Enter a sports league acronym: ").upper()
    if user_input not in sports_leagues.keys():
        print(f"There is no league named {user_input}")
    else:
        print(f"The {sports_leagues[user_input]} has been removed")
        sports_leagues.pop(user_input)


def add_league():
    """
    Adds a new league to the sports_league dictionary. Prompts the user for key and value , if the key already exist
    it prints an error message
    :return:None
    """
    global sports_leagues
    key_input = input("Enter a new sports league acronym: ").upper()
    if key_input in sports_leagues.keys():
        print(f"{key_input} is already listed as {sports_leagues[key_input]}")
    else:
        value_input = input("Enter the name of the new sports league: ")
        sports_leagues[key_input] = value_input


def get_abbreviations():
    """
    Returns a list of all sport leagues abbreviations (sports_league keys)
    :return: List of abbreviations
    """
    global sports_leagues
    sport_league_abbreviations = list(sports_leagues.keys())
    return sport_league_abbreviations


def get_league_descriptions():
    """
    Returns a tuple with all the sport_league descriptions (sports_league descriptions)
    :return: tuple of descriptions
    """
    global sports_leagues
    sport_leagues_descriptions = tuple(sports_leagues.values())
    return sport_leagues_descriptions


def get_league_abbreviations_and_descriptions():
    """
    Returns a set of all sport_leagues keys and values
    :return:
    """
    global sports_leagues
    league_set = set()
    for keys, values in sports_leagues.items():
        league_set.add(f"{keys} is the {values}")
    return league_set


def main():
    # Test 1: Delete a non existent league : Input ABC
    delete_league()
    # Test 2: Delete the NHL
    delete_league()
    # Test 3 Add an existing league : Input MLS
    add_league()
    # Test 4 Add a new league : Input FIFA , Federacion Internacional De Futbol Asociado
    add_league()
    league_abbreviations = get_abbreviations()
    print(league_abbreviations)
    league_descriptions = get_league_descriptions()
    print(league_descriptions)
    league_abbreviations_descriptions = get_league_abbreviations_and_descriptions()
    print(league_abbreviations_descriptions)


if __name__ == "__main__":
    main()

