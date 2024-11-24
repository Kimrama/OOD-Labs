class Path_Finder_Queue :
    def __init__(self, start, end, width, height) :
        
        if start == None : 
            print("Invalid map input.")
            self.queue = []
        else : self.queue = [start]
        self.end = end
        self.width = width
        self.height = height
        self.record_part = []

    def enQ(self, i) :
        self.queue.append(i)

    def deQ(self, room) :
        print(f"Queue: {self.queue}")
        position = self.queue.pop(0)
        state = self.look_around(position, room)
        if state == "end" : 
            print("Found the exit portal.")
            q.queue = []
        elif self.isEmpty() : print("Cannot reach the exit portal.")

    def isEmpty(self) :
        return len(self.queue) == 0

    def look_around(self, current_position, room) :
        # N
        if current_position[1] - 1 >= 0 \
            and (current_position[0], current_position[1] - 1) \
                not in self.record_part :
            if room[current_position[1] - 1][current_position[0]] == '_' :
                self.enQ((current_position[0], current_position[1] - 1))
                self.record_part.append((current_position[0], current_position[1] - 1))
            elif room[current_position[1] - 1][current_position[0]] == 'O' :
                return "end"

        # E
        if current_position[0] + 1 <= width - 1\
            and (current_position[0] + 1, current_position[1]) \
                not in self.record_part :
            if room[current_position[1]][current_position[0] + 1] == '_' :
                self.enQ((current_position[0] + 1, current_position[1]))
                self.record_part.append((current_position[0] + 1, current_position[1]))
            elif room[current_position[1]][current_position[0] + 1] == 'O' :
                return "end"

        # S
        if current_position[1] + 1 <= height - 1 \
            and (current_position[0], current_position[1] + 1) \
                not in self.record_part :
            if room[current_position[1] + 1][current_position[0]] == '_' :
                self.enQ((current_position[0], current_position[1] + 1))
                self.record_part.append((current_position[0], current_position[1] + 1))
            elif room[current_position[1] + 1][current_position[0]] == 'O' :
                return "end"

        # W
        if current_position[0] - 1 >= 0 \
            and (current_position[0] - 1, current_position[1]) \
                not in self.record_part :
            if room[current_position[1]][current_position[0] - 1] == '_' :
                self.enQ((current_position[0] - 1, current_position[1]))
                self.record_part.append((current_position[0] - 1, current_position[1]))
            elif room[current_position[1]][current_position[0] - 1] == 'O' :
                return "end"
    
room = input("Enter width, height, and room: ").split(" ")
width = int(room[0])
height = int(room[1])

room = room[2].split(",")

check = True

#validate room
if len(room) != height : 
    print("Invalid map input.")
    check = False
for i in room :
    if len(i) != width : 
        print("Invalid map input.")
        check = False
        break

if check != False :
    def search(room) :
        position = {'start': None, 'end': None}
        for x in range(width) :
            for y in range(height) :
                if room[y][x] == 'F' :
                    position["start"] = (x, y)
                elif room[y][x] == 'O' :
                    position["end"] = (x, y)
        return position

    position_set = search(room)

    q = Path_Finder_Queue(position_set["start"], position_set["end"], width, height)

    while not q.isEmpty() :
        q.deQ(room)