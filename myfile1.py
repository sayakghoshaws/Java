
def list_benefits():
    benefit_list = ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]
    return (benefit_list)
dir(list_benefits)
def build_sentence(info):
    return ("%s"% (info)+" is a benefit of functions!")
def name_the_benefit_of_functions():
    list_of_benefits = list_benefits()

    for benefit in list_of_benefits:
        print (build_sentence(benefit))
#########################################
#name_the_benefit_of_functions()

#Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000
car2.name = "jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000
####################### ############
print(car1.description())
print(car2.description())

#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.)
#instead of using its index to address it.
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
#print(phonebook)
#del phonebook["John"]
#phonebook.pop("John")
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
if "Jack" in phonebook:
    print("Jack is listed in the phonebook.")

scorecard = {}
scorecard["eng"] = 90
scorecard["phy"] = 95

print(a-b*c**2%d)
for x,y in scorecard.items():
    print(x,y)





     
