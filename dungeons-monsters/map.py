class Map:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        if not Map._initialized:
            with open("map.txt", 'r') as file:
                lines = file.read().splitlines()
                self._map = [list(line) for line in lines]
            self._revealed = [[False] * len(row) for row in self._map]
            Map._initialized = True

    def __getitem__(self, row):
        return self._map[row]

    def __len__(self):
        return len(self._map)

    def show_map(self, loc):
        result = ""
        for r in range(5):
            for c in range(5):
                if (r, c) == (loc[0], loc[1]):
                    result += '* '
                elif self._revealed[r][c]:
                    result += (f'{self._map[r][c]} ')
                else:
                    result += 'x '
            result += '\n'
        return result

    def reveal(self, loc):
        self._revealed[loc[0]][loc[1]] = True
    
    def remove_at_loc(self, loc):
        self[loc[0]][loc[1]] = 'n'