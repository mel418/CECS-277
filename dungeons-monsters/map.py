class Map:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)
            cls._instance.map = []
            cls._instance.revealed = []
        return cls._instance
    
    def __init__(self) -> None:
        with open("map.txt", 'r') as file:
            lines = file.read().splitlines()
            self.map = [list(line) for line in lines]
            self.revealed = [[False] * len(row) for row in self.map]

    def __getitem__(self, row):
        return self.map[row]

    def __len__(self):
        return len(self.map)

    def show_map(self, loc):
        result = ""
        for r in range(5):
            for c in range(5):
                if (r, c) == loc:
                    result += '*'
                elif self.revealed[r][c]:
                    result += self.map[r][c]
                else:
                    result += 'x'
            result += '\n'
        return result

    def reveal(self, loc):
        r, c = loc
        self.revealed[r][c] = True
    
    def remove_at_loc(self, loc):
        r, c = loc
        self.map[r][c] = 'n'

# Example usage
# map_singleton = Map()
# print(map_singleton[0])  # Access the first row of the map
# print(len(map_singleton))  # Get the number of rows in the map
# print(map_singleton.show_map((1, 1)))  # Show the map with the hero at (2, 2)
# map_singleton.reveal((1, 1))  # Reveal a location
# map_singleton.remove_at_loc((3, 3))  # Remove a character at a location
# print(map_singleton.show_map((3, 3)))