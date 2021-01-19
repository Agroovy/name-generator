#This is the module which generates names
import json
from random import choice, choices

#-----------------------------------------------------------Functions
def random_bool(true_chance, false_chance):
    #This is easier to look at than writing it out
    return(choices([True, False], weights=(true_chance, false_chance))[0]) 

def name():
    #This function returns a generated name

    #--------------------------------------------------------Get all data
    #Get the full name and gender choice. 
    #This inside the function because the data has to be re-read every call
    #Settings can be changed while main.py is running

    with open("config.json", "r") as read_file:
        settings = json.load(read_file)

    f = settings["first_name"]
    m = settings["middle_name"]
    l = settings["last_name"]
    male_names = settings["m"]
    female_names = settings["f"]

    #Read all of the name data. Gets adjective lists, nouns lists, and the domain list
    with open("name_parts.json", "r") as read_file:
        terms = json.load(read_file)

    f_adj = terms["female_adjectives"]
    m_adj = terms["male_adjectives"]
    g_adj = terms["genderless_adjectives"]

    f_noun = terms["female_nouns"]
    m_noun = terms["male_nouns"]
    g_noun = terms["genderless_nouns"]

    all_domains = terms["domains"]

    #Choose the adjective, noun, and domain to use
    #The gender choice allows for both genders to be chosen or neither gender
    #Either way, the genderless words will be used. This chooses which words to add on

    added_nouns = []
    added_adjectives = []

    if male_names:
        added_adjectives += m_adj
        added_nouns += m_noun

    if female_names:
        added_adjectives += f_adj
        added_nouns += f_noun
    
    #Choose what name format to use. Full name, first name, or last name
    used_name = choices(
        [
            #If there"s no middle name, don"t try to add one
            ("{} {}".format(f,l) if m == "" else "{} {} {}".format(f,m,l)),
            "{}".format(f),
            "{}".format(l)
        ],
        weights=[80,10,10]
    )[0]
    
    #This chooses a random element from the list and makes a name out of the choices
    
    adjective = choice(g_adj + added_adjectives)
    noun = choice(g_noun + added_nouns)
    domain = choice(all_domains)

    name =(
        "The "
        + (adjective + " " if random_bool(95,5) else "")
        + (noun + " " if random_bool(95,5) else "")
        + used_name
        + (" of " + domain if random_bool(50,50) else "")
    )
    
    return(name)
