import queue
import random
import time

request_queue = queue.Queue()
request_id_counter = 1


def generate_request():
    global request_id_counter

    request = f"Request {request_id_counter}"
    request_id_counter += 1

    request_queue.put(request)
    print(f"Generated and added to queue: {request}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()

        print(f"Processing {request}")
        time.sleep(1)
    else:
        print("No requests available to process.")


def main():
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 2))

            process_request()
    except KeyboardInterrupt:
        print("\nExiting the program...")


if __name__ == "__main__":
    main()
