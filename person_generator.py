import random

def get_first_name_en():
    first_names = ['Aaron', 'Abraham', 'Adam', 'Adrian', 'Aidan','Alan','Albert','Alejandro','Alex','Alexander','Alfred','Andrew','Angel',\
            'Anthony','Antonio','Ashton','Austin','Abigail','Ada','Adelina','Agatha','Alexa','Alexandra','Alexis','Alise','Allison',\
            'Alyssa','Amanda','Amber','Amelia','Angelina','Anita','Ann','Ariana','Arianna','Ashley','Audrey','Autumn','Ava','Avery',\
            'Benjamin','Bernard','Blake','Brandon','Brian','Bruce','Bryan','Bailey','Barbara','Beatrice','Belinda','Brianna','Bridjet',\
            'Brooke','Cameron','Carl','Carlos','Charles','Christopher','Cole','Connor','Caleb','Carter','Chase','Christian','Clifford',\
            'Cody','Colin','Curtis','Cyrus','Caroline','Catherine','Cecilia','Celia','Chloe','Christine','Claire','Daniel','David',\
            'Dennis','Devin','Diego','Dominic','Donald','Douglas','Dylan','Daisy','Danielle','Deborah','Delia','Destiny','Diana',\
            'Dorothy','Edward','Elijah','Eric','Ethan','Evan','Eleanor','Elizabeth','Ella','Emily','Emma','Erin','Evelyn','Francis',\
            'Fred','Faith','Fiona','Florence','Freda','Gabriel','Gavin','Geoffrey','George','Gerld','Gilbert','Gordon','Graham','Gregory',\
            'Gloria','Gabriella','Gabrielle','Gladys','Grace','Harold','Harry','Hayden','Henry','Herbert','Horace','Howard','Hugh',\
            'Hunter','Hailey','Haley','Hannah','Helen','Ian','Isaac','Isaiah','Isabel','Isabella','Jack','Jackson','Jacob','Jaden','Jake',\
            'James','Jason','Jayden','Jeffery','Jeremiah','Jesse','Jesus','John','Jonathan','Jordan','Jose','Joseph','Joshua','Juan',\
            'Julian','Justin','Jacqueline','Jada','Jane','Jasmine','Jenna','Jennifer','Jessica','Jocelyn','Jordan','Josephine','Joyce',\
            'Julia','Keith','Kevin','Kyle','Kaitlyn','Katelyn','Katherine','Kathryn','Kayla','Kaylee','Kimberly','Kylie','Landon',\
            'Lawrence','Leonars','Lewis','Logan','Louis','Lucas','Luke','Laura','Lauren','Leah','Leonora','Leslie','Lillian','Lily',\
            'Linda','Lorna','Luccile','Lucy','Lynn','Malcolm','Martin','Mason','Matthew','Michael','Miguel','Miles','Morgan','Mabel',\
            'Mackenzie','Madeline','Madison','Makayla','Margaret','Maria','Marisa','Marjorie','Mary','Maya','Megan','Melanie','Melissa',\
            'Mia','Michelle','Mildred','Molly','Monica','Nathan','Nathaniel','Neil','Nicholas','Noah','Norman','Nancy','Natalie','Nicole',\
            'Nora','Oliver','Oscar','Oswald','Owen','Olivia','Patrick','Peter','Philip','Paige','Pamela','Patricia','Pauline','Penelope',\
            'Priscilla','Ralph','Raymond','Reginald','Richard','Robert','Rodrigo','Roger','Ronald','Ryan','Rachel','Rebecca','Riley',\
            'Rita','Rosalind','Rose','Samuel','Sean','Sebastian','Seth','Simon','Stanley','Steven','Samantha','Sandra','Sara','Sarah',\
            'Savannah','Sharon','Sheila','Shirley','Sierra','Sofia','Sophia','Stephanie','Susan','Sybil','Sydney','Sylvia','Thomas',\
            'Timothy','Tyler','Taylor','Trinity','Vanessa','Victoria','Violet', 'Virginia', 'Wallace', 'Walter', 'William',\
            'Wyatt', 'Winifred', 'Xavier', 'Yvonne', 'Zachary', 'Zoe']
        
    return random.sample(first_names, 1)[0]

def get_last_name_en():
    last_names = ['Adams','Aldridge','Alexander','Alison','Alix','Allen','Anderson','Bailey','Baker','Barber','Barlow','Barrett',\
    'Bee','Bell','Bennett','Benson','Bentley','Beverly','Black','Bradley,''Brett','Bronte','Brooke','Brooks','Brown','Bruce',\
    'Burgess','Burney','Burns','Byrne','Campbell','Carr','Carson','Carter','Clark','Cole','Collins','Cooper','Cox','Crawford',\
    'Crystal','Davis','Day','Dean','Dee','Eden','Edwards','Ellis','Evans','Farrell','Fisher','Florence','Ford','Foster','Franklin',\
    'George','Gibson','Gordon','Graham','Grant','Green','Haley','Hall','Harris','Hart','Hicks','Hill','Horne','Howard','Hughes',\
    'Hunt','Jackson','James','Jean','Johnson','Jones','Jordan','Joy','Kimberly','King','Knight','Lane','Lewis','Lindsay','Little',\
    'Love','Lynn','Martin','Meredith','Miller','Mills','Mitchell','Moore','Morgan','Nelson','Norman','Palmer','Peters','Phillips',\
    'Ray','Roberts','Robin','Robinson','Scott','Simon','Smith','Starr','Stevens','Stone','Taylor','Thomas','Toni','Tucker','Walker',\
    'Wallace','Ward','Washington','Waters','West','White','Williams','Wilson','Wright','Young']
        
    return random.sample(last_names, 1)[0]

def get_simple_login():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "-"

    main_use_for = lower_case + upper_case + numbers
    lenght_for_pass = 10
    login = "".join(random.sample(main_use_for, lenght_for_pass))
        
    return login