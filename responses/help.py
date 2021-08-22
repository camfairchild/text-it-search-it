def help_message() -> str:
    """Return a list of commands"""
    return "List of commands:\n" +\
        "/date <location> - Returns the date in the location proceeding the command\n" +\
        "/directions <starting point> <destination> - Returns a list of directions from a starting location to a destination\n" +\
        "/joke - Returns a random joke\n" +\
        "/news - Returns a list of world news articles from the NY Times\n" +\
        "/time <location> - Returns the time in the location proceeding the command\n" +\
        "/translate <text> -> <language> - Translates the text proceeding the command\n" +\
        "/weather <location> - Returns the weather in the city proceeding the command\n" +\
        "<query> - Returns a list of results from a Google search\n"