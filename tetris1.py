shapes = {
    'Q': [['#', '#'],
          ['#', '#']],
    'Z': [['#', '#', '.'],
          ['.', '#', '#']],
    'S': [['.', '#', '#'],
          ['#', '#', '.']],
    'T': [['#', '#', '#'],
          ['.', '#', '.']],
    'I': [['#', '#', '#', '#']],
    'L': [['#', '.'],
          ['#', '.'],
          ['#', '#']],
    'J': [['.', '#'],
          ['.', '#'],
          ['#', '#']]
}


class Piece:
    def __init__(self, piece):
        self.piece = piece

    @property
    def width(self):
        return len(self.piece[0])

    @property
    def height(self):
        return len(self.piece)

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.piece)


class Grid:
    def __init__(self, width, height):
        self.max_height = height
        self.max_width = width
        self.grid = [['.'] * width for __ in range(height)]

    def completed_line(self):
        """Find all fully completed lines in the grid."""
        return [i for i, line in enumerate(self.grid) if line.count('#') == self.max_width]

    def clear_line(self, index):
        """Clear the given line and shift everything above it down."""
        del self.grid[index]
        self.grid.insert(0, ['.' for _ in range(self.max_width)])

    def drop(self, piece, start_column):
        """Determine where the piece will land and return the drop row."""
        for row in range(self.max_height - piece.height + 1):
            for i in range(piece.height):
                for j in range(piece.width):
                    if self.grid[row + i][start_column + j] == "#" and piece.piece[i][j] == "#":
                        return row - 1
        return self.max_height - piece.height

    def place_piece(self, piece, start_column):
        """Place the piece on the grid."""
        drop_row = self.drop(piece, start_column)
        for i in range(piece.height):
            for j in range(piece.width):
                if piece.piece[i][j] == "#":
                    self.grid[drop_row + i][start_column + j] = "#"
        return drop_row

    def display_grid(self):
        """Display the grid with borders."""
        output = []

        output.append("┌" + "─" * self.max_width + "┐")

        for row in self.grid:
            output.append("│" + ''.join(row).replace('.', ' ') + "│")

        output.append("└" + "─" * self.max_width + "┘")

        output.append(" " + "".join(map(str, range(self.max_width)))+ " ")
        return output


def side_by_side_display_with_arrows(steps, labels):
    """Display grids side by side with labels and arrows, perfectly aligned."""

    labeled_grids = []
    for i, (label, grid) in enumerate(zip(labels, steps)):
        arrow = "──►    " if i < len(labels) - 1 else "      |"
        labeled_grids.append([f"{"| "+label} {arrow}"] + grid)


    max_lines = max(len(grid) for grid in labeled_grids)

    padded_grids = [
        grid + [" " * len(grid[0])] * (max_lines - len(grid)) for grid in labeled_grids
    ]


    grids_with_arrows = ["  ".join(row) for row in zip(*padded_grids)]

    return "\n".join(grids_with_arrows)


def tetris_simulation(sequence):
    """Simulate the Tetris game and display grids side by side with labels, while saving the output to a file."""
    grid = Grid(10, 5)
    steps = []
    labels = []
    output = []

    # Add the input sequence to the output
    input_sequence_output = f"Input sequence: {sequence}\n"
    output.append(input_sequence_output)
    print(input_sequence_output)

    for action in sequence.split(','):
        shape, start_column = action[0], int(action[1])
        piece = Piece(shapes[shape])


        grid.place_piece(piece, start_column)
        steps.append(grid.display_grid())
        labels.append(f"{shape}{start_column}")


        while grid.completed_line():
            for line in grid.completed_line():
                grid.clear_line(line)


    steps_output = side_by_side_display_with_arrows(steps, labels)
    print(steps_output)
    output.append(steps_output)

    # Display the final grid state
    final_grid_output = "\nFinal Grid:\n" + "\n".join(grid.display_grid())
    print(final_grid_output)
    output.append(final_grid_output)


    final_height = sum(1 for row in grid.grid if any(cell == "#" for cell in row))
    final_output = f"\n\nTherefore, the output row for this sequence is \"{final_height}\".\n\n"
    print(final_output)
    output.append(final_output)


    with open("output1.txt", "a+", encoding="utf-8") as file:
        file.write("\n".join(output))
        file.write("\n" + "=" * 50 + "\n")



def main():
    print("Example Simulation")
    # Ask the user for input dynamically
    sequence = input("Enter the sequence (e.g.Q0,I2,I6,I0,T4,Q8): ").strip()
    tetris_simulation(sequence)


if __name__ == "__main__":
    main()


















