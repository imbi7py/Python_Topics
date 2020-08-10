#!/usr/bin/env python3
"""Wait for a worker process.
"""

#end_pymotw_header
______ os
______ sys
______ time

___ i __ range(2):
    print('PARENT {}: Forking {}'.f..(os.getpid(), i))
    worker_pid = os.fork()
    if not worker_pid:
        print('WORKER {}: Starting'.f..(i))
        time.sleep(2 + i)
        print('WORKER {}: Finishing'.f..(i))
        sys.exit(i)

___ i __ range(2):
    print('PARENT: Waiting for {}'.f..(i))
    done = os.wait()
    print('PARENT: Child done:', done)
