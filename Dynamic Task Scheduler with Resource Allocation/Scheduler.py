import heapq
import time

class Task:
    def __init__(self, id, priority, resources_needed):
        self.id = i
        self.priority = priority
        self.resources_needed = resources_needed
        self.start_time = None
        self.end_time = None

class Scheduler:
    def __init__(self):
        self.tasks = []
        self.current_time = 0

    def add_task(self, task):
        heapq.heappush(self.tasks, (task.priority, task))

    def allocate_resources(self, task):
        # Simulate resource allocation
        time.sleep(0.1)  # Simulating resource allocation time
        task.start_time = self.current_time
        task.end_time = self.current_time + 1

    def run_scheduler(self):
        while self.tasks:
            _, task = heapq.heappop(self.tasks)
            print(f"Allocating resources for task {task.id}")
            self.allocate_resources(task)
            print(f"Task {task.id} completed in {task.end_time - task.start_time} units of time.")

def main():
    scheduler = Scheduler()

    task1 = Task(1, 2, {'cpu': 2, 'memory': 4})
    task2 = Task(2, 1, {'cpu': 1, 'memory': 2})
    task3 = Task(3, 3, {'cpu': 3, 'memory': 3})

    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    scheduler.run_scheduler()

if __name__ == "__main__":
    main()
