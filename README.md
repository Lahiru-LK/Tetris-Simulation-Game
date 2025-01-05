

---

# 🕹️ Tetris Simulation Game

Welcome to the **Tetris Simulation Game**! 🎮 This is a Python implementation of a simplified Tetris game engine that simulates piece placement, gravity, and row clearing. 🧩

https://github.com/user-attachments/assets/6ee62890-9512-4da1-a52c-a3b1ddd92d77

---

## 📖 Problem Description

The engine models a grid that pieces enter from top and come to rest at the bottom, as if pulled down by gravity. Each piece is made up of four unit squares.
No two unit squares occupy the same space in the grid at the same time.
The pieces are rigid, and come to rest as soon as any part of a piece contacts the bottom of the grid or any resting block. As in Tetris, whenever an entire row of the grid is filled, it disappears, and any higher rows drop into the vacated space without any change to the internal pattern of blocks in any row.
The exe file process a text of lines each representing a sequence of pieces entering the grid.
For each line of the input programs output the resulting height of the remaining blocks within the grid.
The file denotes the different possible shapes by letter. The letters used are Q, Z, S, T, I, L, and J. The shapes of the pieces they represent are shown in the table below:

</td>
</tr>
</table>
<table>
  <tr>
    <td>Letter</td>
    <td>Q</td>
    <td>Z</td>
    <td>S</td>
    <td>T</td>
    <td>I</td>
    <td>L</td>
    <td>J</td>
  </tr>
  <tr>
    <td>Shape</td>
    <td>
      <pre>
##
##
      </pre>
    </td>
    <td>
      <pre>
##
 ##
      </pre>
    </td>
    <td>
      <pre>
 ##
##
      </pre>
    </td>
    <td>
      <pre>
###
 #
      </pre>
    </td>
    <td>
      <pre>
####
      </pre>
    </td>
    <td>
      <pre>
#
#
##
      </pre>
    </td>
    <td>
      <pre>
 #
 #
##
      </pre>
    </td>
  </tr>
</table>

The program does not validate its input for now and assumes that there will be no illegal characters
Moreover, the script does not account for shape rotation in your model. The pieces will always have the orientations shown above.
Each line of the input file is a comma-separated list.
Each entry in the list is a single letter (from the set above) and a single-digit integer. The integer represents the left-most column of the grid that the shape occupies, starting from zero.
The grid of the game space is 10 units wide. For each line of the file, the grid’s initial state is empty.

For example, if the input file consisted of the line “Q0” the corresponding line in the output file would be “2”, since the block will drop to the bottom of the initially empty grid and has height two.

## Examples

### Example 1

A line in the input file contains `I0,I4,Q8` resulting in the following configuration:

```
  I0 │          │ I4  │          │ Q8  │          │
     │          │ ──► │          │ ──► │        ##│
     │####      │     │########  │     │##########│
     └──────────┘     └──────────┘     └──────────┘
      0123456789       0123456789       0123456789

```

The filled bottom row then disappears:

```
│          │
│          │
│        ##│
└──────────┘
 0123456789
```

Therefore, the output row for this sequence is “1”.

### Example 2

A line in the input file contains `T1,Z3,I4`.

```

     │          │       │          │       │    ####  │
  T1 │          │  Z3   │   ##     │  I4   │   ##     │
     │ ###      │  ──►  │ #####    │  ──►  │ #####    │
     │  #       │       │  #       │       │  #       │
     └──────────┘       └──────────┘       └──────────┘
      0123456789         0123456789         0123456789

```

## 🛠️ Features

- ✅ Simulates gravity, block stacking, and row clearing.  
- ✅ Handles multiple sequences of Tetris moves.  
- ✅ Displays the grid evolution step by step.  
- ✅ Outputs the final block height for each input sequence.  

---

## 🚀 Getting Started

### 🐍 Dependencies
- Python 3.x

### 📦 Installation
Clone the repository and navigate to the project directory:  
```bash
git clone https://github.com/your-username/tetris-simulation.git
cd tetris-simulation
```

---

## ▶️ Usage

### 🔧 Run the Simulation

Replace `input.txt` with your desired input, and the game output will be saved in `output.txt`.

1. Make the script executable:  
   ```bash
   chmod +x tetris.py
   ```

2. Execute the program:  
   ```bash
   python3 tetris.py
   ```

3. Input a sequence of moves (e.g., `Q0,I4,T3`) to see the simulation in action.  

---



## 🧪 Running Test Cases

You can test the program using predefined test scenarios:

1. Modify the test case file `sample_test.py` if necessary.  
2. Run the test:  
   ```bash
   python3 sample_test.py
   ```

---

## 📊 Shapes Reference

| Letter | Shape  |
|--------|--------|
| **Q**  | ▩▩ <br> ▩▩ |
| **Z**  | ▩▩.<br>.▩▩ |
| **S**  | .▩▩<br>▩▩. |
| **T**  | ▩▩▩<br>.▩. |
| **I**  | ▩▩▩▩ |
| **L**  | ▩.<br>▩.<br>▩▩ |
| **J**  | .▩<br>.▩<br>▩▩ |

---

## 🎉 Example

Input sequence: `I0,I4,Q8`

- **Step 1:** Place `I0`  
- **Step 2:** Place `I4`  
- **Step 3:** Place `Q8`  

### Visualization
```plaintext
Step 1       Step 2       Step 3
│####      │     │########  │
└──────────┘     └──────────┘
```

Final Height: **1**

---

## 💡 How It Works

- **Gravity:** Pieces fall to the lowest unoccupied position.  
- **Row Clearing:** Full rows are removed, and higher rows shift down.  
- **Column Selection:** Each piece's placement is based on its starting column.  

---

## 📁 File Structure

```
tetris-simulation/
│
├── tetris.py           # Main script
├── tetris1.py           # Main script
├── tetris2.py           # Main script
├── README.md           # Documentation
└── input.txt          # Simulation outputs
```

---

## 🙌 Contributing

We welcome contributions!  
Feel free to fork the repository, make changes, and create a pull request.  

---

## 📜 License

This project is licensed under the MIT License. 📝

---

## 🎯 Author

Developed with ❤️ by [Your Name](https://github.com/your-username).  

---
