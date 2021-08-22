def help_message() -> str:
    """Return a list of commands"""
    return "/date <loc> - date in loc\n" +\
        "/directions <locA> <locB> - directions from A to B\n" +\
        "/joke - a joke\n" +\
        "/news - lst of news frm NYT\n" +\
        "/time <loc> - time at loc\n" +\
        "/translate <txt> -> <lang>\n" +\
        "/weather <loc> - weather at loc\n" +\
        "<query> - list of results frm Google\n"