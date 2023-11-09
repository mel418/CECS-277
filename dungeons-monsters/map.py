class Map:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        if not Map._initialized:
            self.load_map(1)


    def load_map(self, map_num):
        print(f'map{map_num}.txt')
        with open(f"map{map_num}.txt", 'r') as file:
            lines = file.read().splitlines()
            self._map = [list(line) for line in lines]
        self._revealed = [[False] * len(row) for row in self._map]
        Map._initialized = True

    def __getitem__(self, row):
        return self._map[row]

    def __len__(self):
        return len(self._map)

    def show_map(self, loc):
        map_display = '\n'.join([' '.join(['*' if (r, c) == (loc[0], loc[1]) else self._map[r][c] if self._revealed[r][c] else 'x' for c in range(len(self._map[r]))]) for r in range(len(self._map))])

        return map_display


    def reveal(self, loc):
        self._revealed[loc[0]][loc[1]] = True
    
    def remove_at_loc(self, loc):
        self[loc[0]][loc[1]] = 'n'