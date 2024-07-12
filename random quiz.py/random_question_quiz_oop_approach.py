import random 
from questions import programming_questions, science_questions, math_questions

class Questions_Category():
    # initialize variables
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions
        self.score = 0
        
    def ask_questions(self, num_questions):
        # convert the dict of questions keys into list
        question_keys = list(self.questions.keys())
        
        for i in range(num_questions):
            if not question_keys:
                break
            
            # randomly choice a key / questions
            question = random.choice(question_keys)
            
            print(f"Question {i + 1}: {question}")
            answer = input("Answer: ").strip().lower()
            
            # compare if the answer is right on the value of the key dict[key]
            if answer == str(self.questions[question]).lower():
                print("Correct!\n")
                self.score += 1
            
            else:
                print(f"Wrong! The correct answer is {str(self.questions[question])}\n")
                
            question_keys.remove(question)
        
    def get_score(self):
        return self.score
    
class Quiz:
    def __init__(self):
        # initialize the categories and pass the parameters category and question associated to those category
        self.categories = {
            "Programming": Questions_Category("Programming", programming_questions),
            "Math": Questions_Category("Math", math_questions),
            "Science": Questions_Category("Science", science_questions)
        }
        
    def choose_category(self, num_of_questions):
        if not self.categories:
            print("No categories available.")
            return 
        
        category_ans = input(f"\nChoose a category to answer: {str(list(self.categories.keys()))}\n").strip().capitalize()
        
        if category_ans in self.categories:
            # select the key of inputed category dict[key]. And the selected key / category is passed on Questions_Category that is used in ask_question
            category = self.categories[category_ans]
            # show the question with the selected key / category and questions
            category.ask_questions(num_of_questions)
            print(f"Your {category.name} score is: {category.get_score()}")
            
        else:
            print("Invalid category.")
            
        self.categories.pop(category_ans)
    def show_overall_score(self):
        overall_score = 0

        for category in self.categories.values():
            overall_score += category.get_score()

        print(f"Your overall score is: {overall_score}")

    def start_quiz(self):
        number_of_items = input("How many items would you like to answer? Type 1: (1 - 10) - Type 2: (1 - 20) - Type q to quit\n").strip()
        
        while True:
            if number_of_items == "1":
                # call the choose_category that contains the category and questions that passed on Questions_Category that is used in ask_question
                self.choose_category(10)
                
            elif number_of_items == "2":
                self.choose_category(20)
                
            elif number_of_items == "q":
                self.show_overall_score()
                break
            
            else:
                print("Invalid input! Please enter 1, 2, or q.")
                
if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()