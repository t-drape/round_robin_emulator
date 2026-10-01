"""
Author: TJ Drape
Purpose: Implement a round robin thread scheduling algorithm emulator
Date: September, 2026
Sources of Help: N/A
"""

class Thread:
    """This class mimics a threads that runs in an operating system"""
    def __init__(self, name: str, frames_required: int):
        self.name = name
        self.frames_required = frames_required
        self.running_frames = frames_required
        self.time_budget = 0


class RoundRobinEmulator:
    """This class mimics a round robin thread scheduling algorithm to trace certain frame situations"""
    def __init__(self, time_quantum: int, threads: list):
        self.time_quantum = time_quantum
        self.thread_queue = threads

    def run_frames(self, num_frames: int):
        frame = 0
        # We need it to run through frame 23
        while (frame < (num_frames+1)):
            # Current thread still has threads frames to use
            # Current thread has not exceeded the time quantum
            # Has not exceeded the frame window
            while(self.thread_queue[0].running_frames != 0 and self.thread_queue[0].time_budget < self.time_quantum and frame < (num_frames+1)):
                print(f"Running frame #{frame}\n")
                print(f"The thread: {self.thread_queue[0].name}, has {self.thread_queue[0].running_frames} frames left")
                print("Thread Queue:")
                for i in range(len(self.thread_queue)):
                    print(f"{self.thread_queue[i].name}")
                frame += 1
                self.thread_queue[0].time_budget += 1
                self.thread_queue[0].running_frames -= 1
                print(f"Now, the thread: {self.thread_queue[0].name}, has {self.thread_queue[0].running_frames} frames left\n\n")

            self.shift_queue()
            self.thread_queue[0].time_budget = 0
            if (self.thread_queue[0].running_frames == 0):
                self.thread_queue[0].running_frames = self.thread_queue[0].frames_required

# Okay, I need to implement a list shifting function that moves the first element to the back, and then shifts all other elements forward one index
    def shift_queue(self):
        first_item = self.thread_queue[0]
        self.thread_queue[:-1] = self.thread_queue[1:]
        self.thread_queue[-1] = first_item

# threads = [Thread("T1",2), Thread("T2", 4), Thread("T3", 1), Thread("T4", 7)]

"""
# Remove the quotes to run this program. This is the first test as described by the assignment.
threads = [Thread("T1", 2), Thread("T2", 4), Thread("T3", 1), Thread("T4", 7)]
os_emulator = RoundRobinEmulator(3, threads)
os_emulator.run_frames(23)
"""

"""
# Remove the quotes to run this program. This is the second test as described by the assignment.
threads = [Thread("T1", 2), Thread("T2", 4), Thread("T3", 5), Thread("T4", 9)]
os_emulator = RoundRobinEmulator(4, threads)
os_emulator.run_frames(39)
"""

# Remove the quotes to run this program. This is the third test as described by the assignment.
threads = [Thread("T1", 2), Thread("T2", 4), Thread("T3", 5), Thread("T4", 9)]
os_emulator = RoundRobinEmulator(2, threads)
os_emulator.run_frames(39)


