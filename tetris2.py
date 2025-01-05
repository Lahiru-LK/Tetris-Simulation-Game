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
        # Top border
        output.append("┌" + "─" * self.max_width + "┐")
        # Grid rows
        for row in self.grid:
            output.append("│" + ''.join(row).replace('.', ' ') + "│")
        # Bottom border
        output.append("└" + "─" * self.max_width + "┘")
        # Column numbers (aligned with spaces)
        output.append(" " + "".join(map(str, range(self.max_width)))+ " ")
        return output


def side_by_side_display_with_arrows(steps, labels):
    """Display grids side by side with labels and arrows, perfectly aligned."""
    # Prepare labeled grids
    labeled_grids = []
    for i, (label, grid) in enumerate(zip(labels, steps)):
        arrow = "──►    " if i < len(labels) - 1 else "      |"
        labeled_grids.append([f"{"| "+label} {arrow}"] + grid)

    # Get the maximum number of lines in any grid (for proper alignment)
    max_lines = max(len(grid) for grid in labeled_grids)

    # Pad all grids to the same height
    padded_grids = [
        grid + [" " * len(grid[0])] * (max_lines - len(grid)) for grid in labeled_grids
    ]

    # Combine all grids side by side
    grids_with_arrows = ["  ".join(row) for row in zip(*padded_grids)]

    return "\n".join(grids_with_arrows)


def tetris_simulation(sequence):
    """Simulate the Tetris game and output just the final row height."""
    grid = Grid(10, 5)  # 10x5 grid
    output = []  # Collect output for writing to a file

    # Process each action in the sequence
    for action in sequence.split(','):
        shape, start_column = action[0], int(action[1])
        piece = Piece(shapes[shape])

        # Place the piece
        grid.place_piece(piece, start_column)

        # Clear completed lines
        while grid.completed_line():
            for line in grid.completed_line():
                grid.clear_line(line)

    # Calculate the final height (rows containing blocks)
    final_height = sum(1 for row in grid.grid if any(cell == "#" for cell in row))

    # Append the final height result to the output list
    output.append(str(final_height))

    return output


def main():
    input_file = "input.txt"
    output_file = "output2.txt"

    # Read the input file
    with open(input_file, "r", encoding="utf-8") as file:
        sequences = file.readlines()

    # Open the output file for writing
    with open(output_file, "w", encoding="utf-8") as file:
        # Process each sequence from the input file
        for sequence in sequences:
            sequence = sequence.strip()  # Remove any trailing newline or spaces
            if sequence:
                result = tetris_simulation(sequence)  # Get the result for the sequence
                file.write("\n".join(result) + "\n")  # Write the result (final row height)

                # Print to the command line as requested
                print(f"Input read: {sequence}")
                print(f"Therefore, the output row for this sequence is \"{result[0]}\".\n")


if __name__ == "__main__":
    main()



