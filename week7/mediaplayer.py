import random
from collections import deque




class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
    def getTitle(self):
        return self.title
    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 
    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))



class Queue:
    def __init__(self):
        self.dataQueue = []

    def enqueue(self, data):
        self.dataQueue.insert(0,data)
    
    def dequeue(self):
        return self.dataQueue.pop()
    
    def peek(self):
        return self.dataQueue[-1]
    
    def isEmpty(self):
        return len(self.dataQueue) == 0
    
    def size(self):
        return len(self.dataQueue)

    def __str__(self):
        outputStr = ''
        for item in self.dataQueue:
            outputStr += str(item)+'\n'
        return outputStr



class Stack:
    def __init__(self):
        self.dataStack = []

    def push(self, data):
        self.dataStack.append(data)
    
    def pop(self):
        return self.dataStack.pop()
    
    def size(self):
        return len(self.dataStack)

    def isEmpty(self):
        return True if self.size() == 0 else False
    
    def peek(self):
        return self.dataStack[-1]
    
    def __str__(self):
        return str(self.dataStack)


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. add Song to playlist")
    print("2. remove song from playlist")
    print("3. PLAY")
    print("4. SKIP")
    print("5. BACK")
    print("6. shuffle")
    print("7. show currently playing song")
    print("8. show current playlist order")
    print("0. EXIT")
    print(47 * "-")

playlist = Queue()

for i in range(10):
    new_song = Song(f'{i}',f'{i}')
    playlist.enqueue(new_song)

while True:
    menu()
    choice = int(input())

    #ADD SONG
    if choice == 1:
        songTitle = input('enter song title: ')
        songArtist = input('enter song artist: ')
        new_song = Song(songTitle,songArtist)
        playlist.enqueue(new_song)
        print(f'successfully added: {songTitle} by {songArtist}')

    #DELETE SONG
    elif choice == 2:
        deleteTitle = input('Enter a Song Name to Delete: ')
        for i in range(playlist.size()):
            if (playlist.peek().getTitle() == deleteTitle):
                playlist.dequeue()
            else:
                playlist.enqueue(playlist.dequeue())
                print(playlist.peek())
        print("song removed rrom playlist \n") 
        print(playlist)

    #PLAY
    elif choice == 3:
        currentSong = playlist.peek()
        print(f"currently playing \n {currentSong}", end=" " '\n')
        print("playing...")  
    
    #SKIP
    elif choice == 4:
        playlist.enqueue(playlist.dequeue())
        print("skip...")
        print('current track: ', playlist.peek())
    
    #GO BACK
    elif choice == 5:
        temp_stack = Stack()
        while not playlist.isEmpty():
            temp_stack.push(playlist.dequeue())
        while not temp_stack.isEmpty():
            playlist.enqueue(temp_stack.pop())
        playlist.enqueue(playlist.dequeue)
        
        print("replay...")
        print(playlist.peek())

        while not playlist.isEmpty():
            temp_stack.push(playlist.dequeue())
        while not temp_stack.isEmpty():
            playlist.enqueue(temp_stack.pop())
        playlist.enqueue(playlist.dequeue)
        # temp_deque = deque()
        # while Song():
        #     temp_deque.append(playlist.dequeue())
        #     temp_deque.reverse()
        # while temp_deque:
        #     playlist.enqueue(temp_deque.pop())
        # playlist.enqueue(playlist.dequeue)
        # print("Replaying....")
        # print(playlist.peek())

    #SHUFFLE
    elif choice == 6:
        for i in range(10):
            removeSong = random.randint(0, playlist.size())
            holdSong = playlist.dequeue()
            for j in range(removeSong):
                playlist.enqueue(playlist.dequeue())
            playlist.enqueue(holdSong)
        print("shuffle...")
        print(playlist)

    #CURRENTLY PLAYING        
    elif choice == 7:
        currentSong = playlist.peek()
        print(f"currently playing \n {currentSong}", end=" " '\n')

    #PLAYLIST ORDER    
    elif choice == 8:
        print(playlist)
    elif choice == 0:
        print("Farewell...")
        break
