"""
TO DO STILL:
-----------------------------------------------------------------------------------------------
- finish up string formatting of output citations for MLA, APA, CHIC
- account for error that user does not put a first and last name
- reformat date so that single digit dates dont have a zero in front
- reformat date so that month can be converted into a word, instead of digit representation
-----------------------------------------------------------------------------------------------
"""



""" This function prompts the user to select their desired citation style from one of the 
following options. The function then validates the choice and stores it for later usage. """
from re import M


def askForInput():

    print("Please select your desired citation style")
    print("(M) MLA")
    print("(A) APA")
    print("(C) Chicago")
    print("(X) Exit Program")
    citeStyle = (input("Which style would you like to cite in?: ")).upper()
    print("")

    # Closing program if user wants to quit
    if citeStyle == "x".upper():
        exit()

    # Checking validity of user input
    elif (citeStyle != "a".upper() and citeStyle != "c".upper() and citeStyle != "m".upper()):
        print("Invalid citation style. Try again.")
        askForInput()

    # Keeping the user input choice for later
    else:
        # Giving each citation style a full length name (for stylistic reasons in print text)
        citeStyleName = ""
        if citeStyle == "a".upper():
            citeStyleName = "APA"
        elif citeStyle == "m".upper():
            citeStyleName = "MLA"
        elif citeStyle == "c".upper():
            citeStyleName = "Chicago"

        print(citeStyleName, "style selected. Now Let's enter in your citation information.")

        # Asking for parameters for citation build
        url = input("Paste the cite url here: ")
        articleName = input("Enter the name of the article: ")
        siteName = input("Enter the name of the website: ")
        author = input ("Enter the author's first and last name here (Firstname Lastname): ")
        published = input("Enter the date this article was published (DD/MM/YYYY): ")

        # Easier to manipulate authors first and last name if split here first
        firstName = author.split()[0]
        lastName = author.split()[1]

        # Splitting date into day, month, year for later manipulation
        day = published.split('/')[0]
        month = published.split('/')[1]
        year = published.split('/')[2]

        # Assigning months as proper names for formatting purposes
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
                    'august', 'september', 'october', 'november', 'december']

        # If the user enters in 01 as the month, that will give it the value of january
        # because lists start at 0, we subtract one
        """ NOT WORKING YET """
        for i in len(months):
            month = months[(int(month))-1]

        # Routing the program to the appropriate function based on what style was selected
        if citeStyle == "m".upper():
            mla(url, articleName, siteName, firstName, lastName, day, month, year)
        elif citeStyle == "a".upper():
            apa()
        elif citeStyle == "c".upper():
            chicago()
        return (url, articleName, siteName, firstName, lastName, day, month, year)

"""
This function formats the user's citation info in MLA style
------------------------------------------------------------
MLA FORMAT:
Lastname, Firstname. "Article Name." Website Name *in italics*, Day Month. YYYY, URL.
"""
def mla(url, articleName, siteName, firstName, lastName, day, month, year):
    print("-----------------------------------------")
    print(lastName + ", " + firstName + ". \"" + articleName +"\". " + siteName + ", " + day + " " + month + ". " + year + ". " + url + ".")

""" 
This function formats the user's citation info in APA style
------------------------------------------------------------
APA FORMAT:
Lastname, First Initial. (YYYY, Month Day). Title Of Article *in italics*. Website Name. URL. 
"""
def apa(url, articleName, siteName, author, published):
    pass

"""
This function formats the user's citation info in Chicago style
------------------------------------------------------------
Chicago FORMAT:
Site name. Year. "Article Title." Last modified Month Day. URL.
"""
def chicago(url, articleName, siteName, published):
    pass


""" Main function; executes program """
if __name__ == "__main__":
    askForInput()

    