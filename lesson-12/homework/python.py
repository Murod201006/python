# 1
import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    result = []
    result_lock = threading.Lock()
    step = (end - start) // num_threads

    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step if i != num_threads - 1 else end

        def task(s=thread_start, e=thread_end):
            local_result = []
            check_primes(s, e, local_result)
            with result_lock:
                result.extend(local_result)

        thread = threading.Thread(target=task)
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    print("Prime numbers:", result)

# Example
threaded_prime_checker(1, 100, num_threads=4)
# 2
import threading
from collections import Counter

def process_lines(lines, counter, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    with lock:
        counter.update(local_counter)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads
    threads = []
    counter = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i != num_threads - 1 else total_lines
        thread = threading.Thread(target=process_lines, args=(lines[start:end], counter, lock))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    print("Word Frequencies:")
    for word, count in counter.items():
        print(f"{word}: {count}")

# Example
# Save this file first before running:
# threaded_word_count("sample.txt", num_threads=4)
