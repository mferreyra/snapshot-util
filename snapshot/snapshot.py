"""
Monitor your system/server. Output is written to json file and stdout.
Based on psutil module, https://pypi.org/project/psutil/

Make a snapshot of the state of the system, by default each 30 seconds to snapshot.json (configurable):

{"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
"%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
"KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
"KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
"Timestamp": 1624400255}
"""
import argparse
import json
import psutil
import os
import time


def main():
    """Snapshot tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output", type=int, default=20)
    args = parser.parse_args()

    snaps = Snapshots(args.i, args.f, args.n)

    if os.path.exists(args.f): 
        os.remove(args.f)
    os.system('clear')

    for _ in range(args.n):
        snapshot = snaps.make_snapshots()
        with open(args.f, "a") as file:
            json.dump(snapshot, file)
            file.write("\n")
            print(snapshot, end="\r")   
            time.sleep(args.i)


class Snapshots:
    def __init__(self, interval, file_name, total_snapshosts):
        self.interval = interval
        self.file_name = file_name
        self.total_snapshosts = total_snapshosts

    def make_snapshots(self):
        process_running = process_sleeping = process_stopped = process_zombie = 0
        for process in psutil.process_iter():
            if process.status() == psutil.STATUS_RUNNING:
                process_running += 1
            elif process.status() == psutil.STATUS_SLEEPING:
                process_sleeping += 1
            elif process.status() == psutil.STATUS_STOPPED:
                process_stopped += 1
            elif process.status() == psutil.STATUS_ZOMBIE:
                process_zombie += 1

        snapshot = {
            "Tasks": 
                {"total": len(psutil.pids()), 
                "running": process_running,
                "sleeping": process_sleeping,
                "stopped": process_stopped,
                "zombie": process_zombie}, 
            "%CPU": 
                {"user": psutil.cpu_times_percent().user, 
                "system": psutil.cpu_times_percent().system, 
                "idle": psutil.cpu_times_percent().idle},
            "KiB Mem":
                 {"total": int(psutil.virtual_memory().total/1024),
                 "free": int(psutil.virtual_memory().free/1024),
                 "used": int(psutil.virtual_memory().used/1024)},
            "KiB Swap": 
                {"total": int(psutil.swap_memory().total/1024),
                "free": int(psutil.swap_memory().free/1024),
                "used": int(psutil.swap_memory().used/1024)},
            "Timestamp": int(time.time())
        } 

        return snapshot
      

if __name__ == "__main__":
    main()
