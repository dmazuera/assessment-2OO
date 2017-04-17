"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
Abstraction - 
Encapsulation - 
Polymorphism - 



2. What is a class?
- a class is a 

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?




6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each


"""


# Parts 2 through 5:
# Create your classes and class methods


class Students(object):
    """Super class for storing student name and address"""

    def __init__(self, first_name, last_name, address):
        """Initialize melon order attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def__repr__(self):
    	return '<printable representation of class>'



class Questions(object):
    """ask a question and get answer"""
    def __init__(self, first_name, last_name, address):
        """Initialize melon order attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def__repr__(self):
    	return '<printable representation of class>'


    def print_questions(self, first_name, last_name, address):
        """Prints questions to console and prompt user to answer"""
    
        # True or False


class Exam(Student, Questions):
    """use inherited answers from Student and Questions"""

    def __init__(self, species, qty, country_code):
        """Ini"""

        super(Exam, self).__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def__repr__(self):
    	return '<printable representation of class>'



    def new_question(self, questions, correct_answer):
        """Takes a question and adds it to Exam"""

        

    def users_score(self):
        """Administers all Q's and returns user's score (decimal%)."""

        return self.country_code




