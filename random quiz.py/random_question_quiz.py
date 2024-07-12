import random
from questions import programming_questions, science_questions, math_questions

# define the categories and questions
question_category = {
    "Programming": programming_questions,
    "Science": science_questions,
    "Math": math_questions
}

# initialize score
programming_score = 0
science_score = 0
math_score = 0

def ask_ques(questions_dict, category, num_of_ques): # throws the paramenters of our dict of questions and the category
    global programming_score, science_score, math_score
    
    # convert the keys into list
    question_key = list(questions_dict.keys())
    
    # loop on how many questions you need
    for i in range(num_of_ques):
        if not question_key:
            break
        
        # choice random question on our list of keys
        question = random.choice(question_key)
        
        print(f"Question {i + 1}: {question}")
        answer = input("Answer: ").strip()
        
        # compare the user answer to the value of key dict[keys()]
        if answer.lower() == str(questions_dict[question]).lower():
            print("Correct!\n")
            if category == "programming":
                programming_score += 1
            elif category == "science":
                science_score += 1
            elif category == "math":
                math_score += 1

        else:
            print(f"Wrong! The correct answer is {str(questions_dict[question])}\n")
            
        question_key.remove(question)
            
def choose_category(num_question): # function that manage the selected category and number of items
    global question_category, programming_score, science_score, math_questions
    
    question_category_ans = input(f"\nChoose a category to answer: {str(list(question_category.keys()))}\n").strip().capitalize()
    
    if question_category_ans in question_category:
        # call the ask_question to display the question of the desire category, and throw the parameter question_category[question_category_ans] when question_category_ans is our key o get the value which is the questions
        ask_ques(question_category[question_category_ans], question_category_ans.lower(), num_question)
        
        if question_category_ans == "programming":
            print(f"Your programming score is: {programming_score}")
        
        elif question_category_ans == "science":
            print(f"Your science score is: {science_score}")
            
        elif question_category_ans == "math":
            print(f"Your math score is: {math_score}")
            
        question_category.pop(question_category_ans.capitalize())
    else:
        print("Invalid category!\n")
    
def main():
    global programming_score, science_score, math_score
    while True: 
        number_of_items = input(f"How many items would you like to answer? Type 1: (1 - 10) - Type 2: (1 - 20) - Type q to quit\n")

        if number_of_items == "1":
            choose_category(10)
        elif number_of_items == "2":
            choose_category(20)
        elif number_of_items.lower() == "q":
            overall_score = programming_score + science_score + math_score
            
            print(f"Your overall score is: {overall_score}")
            break
        
        else:
            print("Invalid input! Please enter 1, 2, or q.")
      
if __name__ == "__main__":
    main()