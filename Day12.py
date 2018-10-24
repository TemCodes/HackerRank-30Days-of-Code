class Student(Person):

    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__ (self,firstName,lastName,id,scores ):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.scores = scores

    #   Function Name: calculate
    def calculate(self):
        grade = sum(scores)/len(scores)
        if grade < 40:
            return('T')
        if grade < 50:
            return('D')
        if grade < 70:
            return('P')
        if grade < 80:
            return('A')
        if grade < 90:
            return('E')
        if grade <= 100:
            return('O')
    #   Return: A character denoting the grade.
    #
    # Write your function here
