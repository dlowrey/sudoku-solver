class Student:
    def __init__(self, name):
        """Class constructor creates and initializes a Student object"""
        self.name = name
        self.classification = "Sr"
        self.major = "Computer Science"
        self.classes_taken = []

    def add_class(self, course):
        """Add a class to the `classes_taken` list"""
        self.classes_taken.append(course)


    def __str__(self):
        """Method that is used when a Student object is casted to a string

        i.e str(student) would return the string defined in this method
        """
        return "Name: {}\nClassification: {}\nMajor: {}"\
            .format(self.name, self.classification, self.major)



me = Student("Dane")

me.add_class("Math")
me.add_class("Englis")
me.add_class("Spanich")

print(str(me))