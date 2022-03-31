import subprocess
from threading import Timer
# from time import monotonic_ns


def kill_process(process: subprocess.Popen) -> None:
    print(f"killing process {process.pid}")
    return process.kill()


cmd = ['ping', '/n', '10', 'www.google.com']
# ping = subprocess.run(cmd, capture_output=True, check=True)

try:
    ping = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

except OSError as e:
    print(f"OS error: {e}")

except ValueError as e:
    print(f"Value error: {e}")


my_timer = Timer(2, kill_process, kwargs={"process": ping})

try:

    my_timer.start()
    outs, errs = ping.communicate(timeout=1)
    print(ping.returncode)
    print(outs)
    print(errs)

except subprocess.TimeoutExpired as e:
    # kill_process(process=ping)
    print(f"Process timed out: {e}")
    outs, errs = ping.communicate()
    print(ping.pid)
    print(ping.returncode)
    print(outs)
    print(errs)

finally:
    my_timer.cancel()