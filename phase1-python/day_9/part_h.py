
# Part H (stretch): Retry decorator-free. 
# Write flaky() that raises RuntimeError("Network down") randomly about 70% of the time 
# (use random.random() < 0.7) and otherwise returns "OK". 
# Write retry(func, attempts=5) that calls func() until it succeeds,
#  printing "Attempt 1 failed: Network down" and so on, and re-raises the last error if all attempts fail.
#  This is the pattern behind retries in test frameworks.
import random
def flaky():
    if random.random() < 0.7:
        raise RuntimeError("Network Down")
    return "OK"

def retry(func, attempts=5):
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except RuntimeError as e:
            last_error = e
            print(f"Attempt {attempt} failed: {e}")
    raise last_error

retry(flaky)
