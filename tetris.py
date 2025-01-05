import sys

shapes = {
    'Q': [['#', '#'], ['#', '#']],
    'Z': [['#', '#', '.'], ['.', '#', '#']],
    'S': [['.', '#', '#'], ['#', '#', '.']],
    'T': [['#', '#', '#'], ['.', '#', '.']],
    'I': [['#', '#', '#', '#']],
    'L': [['#', '.'], ['#', '.'], ['#', '#']],
    'J': [['.', '#'], ['.', '#'], ['#', '#']]
}

class Grid:
    def __init__(self, width, height):
        self.max_height = height
        self.max_width = width
        self.grid = [['.'] * width for _ in range(height)]

    def completed_line(self):
        return [i for i, line in enumerate(self.grid) if line.count('#') == self.max_width]

    def clear_line(self, index):
        del self.grid[index]
        self.grid.insert(0, ['.' for _ in range(self.max_width)])

    def drop(self, piece, start_column):
        for row in range(self.max_height - piece.height + 1):
            for i in range(piece.height):
                for j in range(piece.width):
                    if self.grid[row + i][start_column + j] == "#" and piece.piece[i][j] == "#":
                        return row - 1
        return self.max_height - piece.height

    def place_piece(self, piece, start_column):
        drop_row = self.drop(piece, start_column)
        for i in range(piece.height):
            for j in range(piece.width):
                if piece.piece[i][j] == "#":
                    self.grid[drop_row + i][start_column + j] = "#"
        return drop_row



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


def tetris_simulation(sequence):
    grid = Grid(10, 5)
    for action in sequence.split(','):
        shape, start_column = action[0], int(action[1])
        piece = Piece(shapes[shape])
        grid.place_piece(piece, start_column)

        while grid.completed_line():
            for line in grid.completed_line():
                grid.clear_line(line)

    final_height = sum(1 for row in grid.grid if any(cell == "#" for cell in row))
    return final_height


def main():
    input_sequence = sys.stdin.read().strip()
    sequences = input_sequence.splitlines()

    results = []
    for sequence in sequences:
        result = tetris_simulation(sequence)
        results.append(str(result))


    print("\n".join(results))


if __name__ == "__main__":
    main()
























