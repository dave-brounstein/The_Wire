import queue

q = queue.Queue()

def add(job):
    q.put(job)

def join():
    q.join()

def worker():
    while True:
        job = q.get()
        print(f'Working on {job}')
        print(f'Finished {job}')
        q.task_done()

def get_sessions(session_id):
    # not implemented
    return []


def get_categories(session_id):
    # not implemented
    return []

def get_by_duration(start_time, duration):
    return get_by_time(start_time, start_time + duration)

def get_by_time(start_time, end_time):
    # not implemented
    return []
