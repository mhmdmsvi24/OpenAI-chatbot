import time


def retry_request(func, max_retries=3, delay=2):
    """
    Retry a function call if it fails due to network issues.
    """
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Max retries exceeded")
