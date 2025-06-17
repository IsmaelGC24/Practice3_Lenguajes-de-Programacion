# chess_game.py
# Requiere: pip install python-chess

import chess
import sys

class MoveNode:
    """Nodo de árbol binario representando un movimiento SAN"""
    def __init__(self, san="Partida"):
        self.san = san
        self.left = None
        self.right = None  

    def add_move(self, san: str, is_white: bool):
        """Añade a la cadena izquierda si es blancas, derecha si es negras, retornando el nuevo nodo."""
        if is_white:
            if self.left is None:
                self.left = MoveNode(san)
                return self.left
            node = self.left
            while node.left:
                node = node.left
            node.left = MoveNode(san)
            return node.left
        else:
            if self.right is None:
                self.right = MoveNode(san)
                return self.right
            node = self.right
            while node.right:
                node = node.right
            node.right = MoveNode(san)
            return node.right

    def display(self):
        """Imprime el árbol con dos ramas: izquierda para blancas, derecha para negras."""
        print(self.san)
        if self.left:
            self._display_chain(self.left, prefix="", connector="├─ ", direction="left")
        if self.right:
            self._display_chain(self.right, prefix="", connector="└─ ", direction="right")

    def _display_chain(self, node, prefix, connector, direction):
        print(f"{prefix}{connector}{node.san}")
        new_prefix = prefix + ("│  " if direction == "left" else "   ")
        if direction == "left" and node.left:
            self._display_chain(node.left, new_prefix, connector, direction)
        elif direction == "right" and node.right:
            self._display_chain(node.right, new_prefix, connector, direction)


def print_board(board):
    """Imprime el tablero con coordenadas y símbolos de piezas unicode, usando ASCII para marco."""
    # Encabezado de archivos
    print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")
    for rank in range(8, 0, -1):
        row = f"{rank} |"
        for file_idx in range(8):
            piece = board.piece_at(chess.square(file_idx, rank-1))
            symbol = piece.unicode_symbol() if piece else '.'
            row += f" {symbol} |"
        print(row)
        print("  +---+---+---+---+---+---+---+---+")


def main():
    board = chess.Board()
    root = MoveNode()
    moves_san = []

    print("\n==== BIENVENIDO A CHESS ====")
    print("Introduce jugadas en SAN (e4, Nf3, O-O, ...)")
    print("Comandos:")
    print("  árbol     → muestra el árbol binario de turnos")
    print("  resultado → lista numerada de jugadas en SAN")
    print("  salir     → termina la partida\n")

    while True:
        # Mostrar tablero personalizado
        print_board(board)
        prompt = "Blanca" if board.turn == chess.WHITE else "Negra"
        cmd = input(f"{prompt} > ").strip()

        if cmd.lower() == "salir":
            print("Fin de la partida.")
            break

        if cmd.lower() == "árbol":
            print("\n🌳 Árbol de movimientos:")
            root.display()
            print()
            continue

        if cmd.lower() == "resultado":
            pgn_str = ""
            for i in range(0, len(moves_san), 2):
                num = i//2 + 1
                white = moves_san[i]
                black = moves_san[i+1] if i+1 < len(moves_san) else ""
                pgn_str += f"{num}. {white} {black} "
            print("\n✅ Movimientos hasta el momento:")
            print(pgn_str.strip() + "\n")
            continue

        try:
            move = board.parse_san(cmd)
        except ValueError:
            print("❌ Movimiento ilegal o formato incorrecto.")
            continue

        san = board.san(move)
        board.push(move)
        moves_san.append(san)

        # Añadir al árbol
        idx = len(moves_san) - 1
        root.add_move(san, idx % 2 == 0)

    print("¡Partida finalizada!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
