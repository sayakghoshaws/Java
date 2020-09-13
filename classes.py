#classes are types custom
student_name ='Bob'
student_id = 1234567

student_names =['Alice','Bob']
student_ids = [123,456]

students =[('Alice',123),('Bob'),456]

class Student:  #type names have capital letters
    def __init__(self,name_list,id):  #magic method gets called automatically,only called once
        #passing just reference of same instance
        self.name_list = name_list
        #passing just reference of same instance
        # self.name = name_list[:]
        # self.name = list(name_list)

        self.id   = id

    def description(self):
        return 'Name: ' + str(self.name_list) + '\n' +'ID: ' + str(self.id)

    def summary(self,grade,course):
        return f'{self.name_list} got a {grade} in {course}'

    # s = Student('Alice',123) #s is instance of a class
    # print(s.summary('A','Calculus'))

    def __str__(self): #also used for print(a)
        ##magic method that is called when str(self) is called
        return f'my list is: {self.name_list}'

    def __repr__(self): #default description
        #return f'Student({self.name_list})'
        return f'Student({self.name_list})'
        #return f'Student({self.name_list!r})'
        #'''this is reper string'''

a = Student('a',123)
str(a)  #'my list is []'
print(a) #my list is []'
