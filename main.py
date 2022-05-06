from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.display()
    quizBrain.nextQuestion()

print("You've completed the quiz!")
print(f"Your final answer was {quizBrain.score}/{len(quizBrain.question_list)}")