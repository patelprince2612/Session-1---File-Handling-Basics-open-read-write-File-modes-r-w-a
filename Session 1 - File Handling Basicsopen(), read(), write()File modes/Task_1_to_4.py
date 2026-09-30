# 1. Create a text file named my_fav_songs.txt using Python's open() function in write ('w') mode, and write the names of your 5 favorite songs into it, each on a new line.
file = open('my_fav_songs.txt', 'w')
file.write("Bohemian Rhapsody\n")
file.write("Stairway to Heaven\n")
file.write("Hotel California\n")
file.write("Smells Like Teen Spirit\n")
file.write("Imagine\n")
file.close()

# 2. Write a Python script that opens the my_fav_songs.txt file in read ('r') mode and prints each song name to the console with its line number (like a playlist).
file = open('my_fav_songs.txt', 'r')
lines = file.readlines()
for i in range(len(lines)):
    print(f"{i + 1}. {lines[i].strip()}")
file.close()

# 3. Add 2 more song names to my_fav_songs.txt without deleting the existing content, using Python's open() function in append ('a') mode.
file = open('my_fav_songs.txt', 'a')
file.write("Hey Jude\n")
file.write("Billie Jean\n")
file.close()

# 4. Build a script that reads all lines from my_fav_songs.txt, counts how many songs are listed, and displays 'Total songs: X' at the end. Hint: Use the readlines() method to get all lines as a list and len() to count.
file = open('my_fav_songs.txt', 'r')
lines = file.readlines()
total_songs = len(lines)
print(f"Total songs: {total_songs}")
file.close()