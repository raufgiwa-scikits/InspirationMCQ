from flask import Flask, render_template, request
import os

app = Flask(__name__,template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

# Define the questions
questions = [
    {   'no':1,
        'question': '1. What is the value of x if 2x + 3 = 7?',
        'choices': ['1', '2', '3', '4'],
        'answer': '2',  # Correct answer
        'explain': 'Correct answer',  # Correct answer
        'Difficulty': 5  # Correct answer
    },
    {   'no':2,
        'question': '2. Which of the following is a synonym for "abundant"?',
        'choices': ['Scarce', 'Plentiful', 'Rare', 'Insufficient'],
        'answer': 'Plentiful',  # Correct answer
        'explain': 'Correct answer',  # Correct answer
        'Difficulty': 1  # Correct answer
    },
    {   'no':3,
        'question': '3. If the area of a circle is 16π, what is its circumference?',
        'choices': ['8π', '16π', '4π', '32π'],
        'answer': '8π',  # Correct answer
        'explain': 'Correct answer' ,  # Correct answer
        'Difficulty': 4  # Correct answer
    },
    {   'no':4,
        'question': '4. In the sentence "She ran quickly," the word "quickly" is what part of speech?',
        'choices': ['Noun', 'Verb', 'Adjective', 'Adverb'],
        'answer': 'Adverb',  # Correct answer
        'explain': 'Correct answer'  ,  # Correct answer
        'Difficulty': 2  # Correct answer
    },
    {   'no':5,
        'question': '5. Which of the following numbers is a prime number?',
        'choices': ['9', '15', '17', '21'],
        'answer': '17',  # Correct answer
        'explain': 'Correct answer'  ,  # Correct answer
        'Difficulty': 3  # Correct answer
    }
]

questions_name=[f"No{i}" for i in range(len(questions))]
questions_no=[f"{i}" for i in range(len(questions))]


@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = {}
        score = 0
        # Iterate over questions to check answers
        for i in range(len(questions)):
            selected = request.form.get(f'question-{i+1}')
            print(selected,"|",questions[i]['answer'])
            user_answers[i] = selected
            if selected == questions[i]['answer']:
                score += 1
        return render_template('result.html', score=score, total=len(questions))
    else:
        return render_template('quiz.html', questions=questions,questions_name=questions_name,questions_no=questions_no)

if __name__ == '__main__':
    app.run(debug=True, port=5000, debug=True)
