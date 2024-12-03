from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self):
        pass

class King(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)

    def can_move(self, new_horizontal, new_vertical):
        if abs(ord(new_horizontal) - ord(self.horizontal)) <= 1 and abs(new_vertical - self.vertical) <= 1:
            return True
        else:
            return False

king = King('e', 3)
print(king.can_move('f', 3))
print(king.can_move('d', 5))

class Knight(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)

    def can_move(self, new_horizontal, new_vertical):
        x = abs(ord(new_horizontal) - ord(self.horizontal))
        y = abs(new_vertical - self.vertical)

        if (x == 2 and y == 1) or (x == 1 and y == 2):
            return True
        else:
            return False

king = King('d', 4)
knight = Knight('b', 1)

print("Король:")
print(f"Можно пойти на d6? {king.can_move('d', 5)}")
print(f"Можно пойти на e3? {king.can_move('e', 7)}")

print("----")

print("Конь:")
print(f"Можно пойти на d3? {knight.can_move('c', 3)}")
print(f"Можно пойти на b2? {knight.can_move('b', 3)}")
