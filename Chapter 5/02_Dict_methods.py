marks= {
    "harry" : 100 ,
    "Walid" : 85 ,
    "Sayam" : 57 ,
    0 : "aziz"
}

# print(marks.items())
# print(marks.keys())
print(marks.values())

marks.update({"Walid" : 92 , "Sami" : 97})
# print(marks)

print(marks.get("Walid"))  #Prints None/Values
print(marks["Walid"]) #prints values/Errors

#marks.clear()
print(marks.pop("Sayam"))
print(marks)
