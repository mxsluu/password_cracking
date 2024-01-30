import multiprocessing
import time
import multiprocessing as mp
from nltk.corpus import words
from bcrypt import hashpw


def crack_password(data, possible_passwords, event):
    data = data.split(":")
    user = data[0]
    user_digest = bytes(data[1], 'utf-8')
    salt = user_digest[0:29]
    for password in possible_passwords:
        if 6 <= len(password) <= 10:
            potential_digest = hashpw(bytes(password, 'utf-8'), salt)
            if potential_digest == user_digest:
                print(user, password)
                event.set()
    return None

def main():
    with open("shadow.txt", "r") as f:
        data = []
        for line in f.readlines():
            data.append(line.rstrip())
    word_bank = words.words()
    start = time.time()
    for i in range(len(data)):
        job_start_time = time.time()
        done = False
        jobs = []
        event = multiprocessing.Event()
        for j in range(0, 236736, 19728):
            job = mp.Process(target=crack_password, args=(data[i], word_bank[j:j+19728], event))
            jobs.append(job)
            job.start()
        while not done:
            if event.is_set():
                done = True
        print("Time taken to crack: %2f s" % (time.time()-job_start_time))
        for job in jobs:
            job.terminate()
    print("Total time: %2f s" % (time.time() - start))

if __name__ == '__main__':
    main()
