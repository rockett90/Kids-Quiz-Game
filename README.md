# Kids-Quiz-Game

A fun and interactive Python quiz game built with Tkinter! This application randomly selects questions from two JSON files (Maths and English), displays them to the user, and checks their answers. Points are awarded for correct answers, and the user can see immediate feedback.

## Features

- Randomly selects questions from two categories: Maths and English.
- Provides immediate feedback on correct or incorrect answers.
- Tracks the user's score throughout the session.
- Simple and user-friendly GUI built with Tkinter.

## Requirements

- Python 3.x
- JSON files containing the questions and answers.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/quiz-game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd quiz-game
   ```

3. Create a folder named `resources` in the project directory.

4. Add two JSON files inside the `resources` folder:
   - `maths_questions.json`
   - `english_questions.json`

5. Populate these JSON files with your questions and answers. Use the following format:

### Example `maths_questions.json`:
```json
[
    {"question": "What is 8 + 5?", "answer": "13"},
    {"question": "What is 15 - 7?", "answer": "8"}
]
```

### Example `english_questions.json`:
```json
[
    {"question": "What is the plural of 'child'?", "answer": "children"},
    {"question": "What is the synonym of 'happy'?", "answer": "joyful"}
]
```

6. Run the program:
   ```bash
   python quiz_game.py
   ```

## How to Use

1. The application will display a random question from either Maths or English.
2. Type your answer in the text box and click "Submit."
3. Receive immediate feedback on whether your answer was correct or incorrect.
4. The next question will appear automatically.
5. Enjoy the game and aim for a high score!

## Customization

- To add more questions, simply edit the `maths_questions.json` and `english_questions.json` files in the `resources` folder.
- You can modify the appearance or functionality of the game by editing the `quiz_game.py` script.

## License

None

## Contributing

Contributions are welcome! If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Open a pull request with a detailed description of your changes.



