# matrix-effect-in-pygame
[![](https://img.shields.io/badge/generated-with_cursor-blue)](https://cursor.sh)<br/>
This project creates a fullscreen Matrix-style rain effect using Pygame. It simulates falling characters that fade and change, creating a visual effect similar to the one seen in "The Matrix" movies.

## NOTICE GENERATED WITH AI
Generated with [cursor](https://cursor.sh) using a couple of prompts.

## Requirements

- Python 3.12 or later
- Pygame library

## Installation

1. Ensure you have Python 3.12 or later installed on your system.
2. Clone this repository or download the `main.py` and `requirements.txt` files.
3. Open a terminal or command prompt and navigate to the project directory.
4. Install the required packages by running:
   ```
   pip install -r requirements.txt
   ```

## How to Run

1. Save the `main.py` file to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `main.py`.
4. Run the script using one of the following commands:

   - For default alphabet:
     ```
     python main.py
     ```
   - For custom alphabet:
     ```
     python main.py "CUSTOMALPHABET123"
     ```

5. To exit the program, press the ESC key.

## How It Works

The Matrix effect is created using the following key components:

1. **Fullscreen Display**: The program uses Pygame to create a fullscreen window with hardware acceleration.

2. **Drop Class**: Each column of falling characters is represented by a `Drop` object. This class manages the position, speed, and appearance of the characters.

3. **Character Management**: 
   - Each drop maintains a list of characters and their opacities.
   - Characters at the top of the drop are brighter and more opaque.
   - As characters fall, they fade out, creating a trailing effect.

4. **Animation Loop**:
   - The main loop continuously updates and draws all drops.
   - Each frame, the drops move down, update their characters, and adjust opacities.
   - Faded characters are replaced with new, bright characters at the top of the drop.

5. **Customization**:
   - The alphabet used for the characters can be customized via command-line argument.
   - Font size, falling speed, and fading speed are adjustable in the code.

6. **Performance**:
   - The program uses Pygame's hardware acceleration features for smooth rendering.
   - A clock is used to maintain a consistent frame rate.

This implementation creates a visually appealing Matrix rain effect that can be customized and runs efficiently on most systems.