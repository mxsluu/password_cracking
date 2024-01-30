from hashlib import sha256
import string
import random
import time


def hashing(input_string, limit):
    input_string = bytes(input_string, 'utf-8')
    sha256_hash_obj = sha256()
    sha256_hash_obj.update(input_string)
    digest = sha256_hash_obj.hexdigest()
    return bin(int(digest, 16))

print(hashing("he", 1))


"""
def find_differences(s1, s2):
    j = 0
    for i in range(64):
        if s1[i] != s2[i]:
            j += 1
    return j

string1 = "Hello World"
string2 = "Hallo World"
print("String 1:", string1)
print("String 2:", string2)
print("Length of strings:", len(string1))
print("Difference in bytes: %d\n" % find_differences(hashing(string2, 256), hashing(string1, 256)))

string3 = "Michael"
string4 = "Micheal"
print("String 1:", string3)
print("String 2:", string4)
print("Length of strings:", len(string3))
print("Difference in bytes: %d\n" % find_differences(hashing(string3, 256), hashing(string4, 256)))

string5 = "csc321"
string6 = "csc320"

print("String 1:", string5)
print("String 2:", string6)
print("Length of strings:", len(string5))
print("Difference in bytes: %d\n" % find_differences(hashing(string5, 256), hashing(string6, 256)))

string7 = "a"
string8 = "b"

print("String 1:", string7)
print("String 2:", string8)
print("Length of strings:", len(string7))
print("Difference in bytes: %d\n" % find_differences(hashing(string7, 256), hashing(string8, 256)))

string9 = "poiauhgiousdhgidsufhgoisdfuhgldskjrhglkdsjhgpioufhdgpsuoidfhglkjsdaisugpufhgpadjfhngpoadifhg"
string10 = "aoiauhgiousdhgidsufhgoisdfuhgldskjrhglkdsjhgpioufhdgpsuoidfhglkjsdaisugpufhgpadjfhngpoadifhg"

print("String 1:", string9)
print("String 2:", string10)
print("Length of strings:", len(string9))
print("Difference in bytes: %d\n" % find_differences(hashing(string9, 256), hashing(string10, 256)))

"""

def find_collision(limit):
    start_time = time.time()
    hashes = {}
    while True:
        length = random.randint(1, 100)
        message = ''.join(random.choices(string.ascii_letters, k=length))
        digest = hashing(message, limit)
        if digest not in hashes:
            hashes[digest] = message
        elif hashes[digest] != message:
            return time.time() - start_time, len(hashes)


times = []
hash_sizes = []
k = 8
while k != 52:
    ret = find_collision(k)
    times.append(ret[0])
    hash_sizes.append(ret[1])
    k += 2

k = 8
for n in range(len(times)):
    print("Hashes done (Number of Inputs): %d\nTime taken: %4f s\nHash Size:%d bits\n" % (hash_sizes[n], times[n], k))
    k += 2
