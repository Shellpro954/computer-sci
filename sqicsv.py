import sqlite3
with sqlite3.connect("hotels.db") as hotel:
    cursor = hotel.cursor()
cursor.execute("""Create table if not exists hoteltest16(
id INTEGER PRIMARY KEY AUTOINCREMENT,
hotel text not null,
location text not null,
country text not null,
region text not null,
company text not null,
scor text not null,
rank integer not null,
rooms integer not null,
theme text not null,
year text not null,
be text not null,
pastrank text not null);""")

 
csv = open("top_hotels.csv","r")
headerline = csv.readline()
#for line in csv:
    
  #  line = line.strip()
 #   line = line.split(",")
  #  newhotel = line[0]
  #  newlocation = line[1]
  #  newcountry = line[2]
  #  newregion = line[3]
  #  newcompany = line[4]
  #  newscor = line[5]
  #  newrank = line[6]
  #  newrooms = line[7]
  #  newtheme = line[8]
  #  newyear = line[9]
  #  newbe = line[10]
  #  newpastrank = line[11]
    
  #  cursor.execute("""Insert into hoteltest16(hotel,location,country,region,company,scor,rank,rooms,theme,year,be,pastrank)
  #  values(?,?,?,?,?,?,?,?,?,?,?,?)""",(newhotel,newlocation,newcountry,newregion,newcompany,newscor,newrank,newrooms,newtheme,newyear,newbe,newpastrank))
  #  hotel.commit()
    
cursor.execute("select * from hoteltest165")
table = (cursor.fetchall())


userchoice = int(input("Pick A Filter To Search By \n - Country: \n - Region: \n - Min Number Of Rooms: \n - name: \n rank range: \n Choice: "))
if userchoice == 1:
    country = input(" Please Enter The Country You Wish To Search By: ")
    for line in table:     
        if country in line:
            print(line)
            
if userchoice == 2:
    Region = input(" Please Enter The Region You Wish To Search By: ")
    for line in table:     
        if Region in line:
            print(line)
            
if userchoice == 3:
    print(table)
    numroom = input("Please Enter The Minimum Number Of Rooms You Wish To Search By: ")
    min_rooms = int(numroom)  
    for line in table:
        print(line[8])
        rooms = int(line[8])
        if rooms >= min_rooms:
            print(line)
            
if userchoice == 4:
    name = input(" Please Enter The Name Of The Hotel You Wish To Search By: ")
    for line in table:
        if name in line:
            print(line)
            
if userchoice == 5:
    Smallrange = int(input(" Please Enter The Lowest Rank You Wish To Search By: "))
    Bigrange = int(input(" Please Enter The Highest Rank You Wish To Search By: "))
    for line in table:
        if Smallrange < line[7] and Bigrange > line[7]:
            print(line)
            
            
