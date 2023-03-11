import subprocess
from io import StringIO
the_host = "127.0.0.1"
ping_result = subprocess.run(
    ["ping","-c","10","-i","1","-n","-q", the_host],
    capture_output=True
)


ping_lines = StringIO(ping_result.stdout.decode()).getvalue().split()
t_names = ping_lines[-4].split("/")
t_vals = ping_lines[-2].split("/")

for name in t_names:
    nameIdx = t_names.index(name)
    new_name = ""
    match(name):
        case "min":
            new_name = "TR_Ping_Min"
        case "avg":
            new_name = "TR_Ping_Avg"
        case "max":
            new_name = "TR_Ping_Max"
        case "mdev":
            new_name = "TR_Ping_StdDev"
    t_names.remove(name)
    t_names.insert(nameIdx, new_name)

rl = dict(zip(t_names, t_vals))
from TestUtils.TestResults import TestResult

result_frame = TestResult("ping")._frame
result_frame["TA_SRC"] = "self"
result_frame["TA_DST"] = the_host
result_frame["TR_Ping_Min"] = rl["TR_Ping_Min"]
result_frame["TR_Ping_Max"] = rl["TR_Ping_Max"]
result_frame["TR_Ping_Min"] = rl["TR_Ping_Avg"]
result_frame["TR_Ping_StdDev"] = rl["TR_Ping_StdDev"]
result_frame["TR_Ping_PctLoss"] = rl["TR_Ping_PctLoss"]