import speedtest
from TestUtils.TestObjects import TestResult
from termcolor import colored, cprint

def speed_runner():
    ''' run speedtest '''
    tester = speedtest.Speedtest()
    speed_template = TestResult("speed").generate_frame()

    server = tester.get_best_server()
    tester.download()
    tester.upload()
    results_url = colored(str(tester.results.share()), "white", "on_blue")
    results = tester.results.dict()
    speed_template["SRC"] = "self"
    speed_template["DST"] = server['sponsor'] + " " + server['name']
    download_speed = round(results['download']/1024/1024,0)
    upload_speed = round(results['upload']/1024/1024,0)
    if download_speed < 50:
        speed_template["Speed_Down"] = colored(str(download_speed) + " Mbps", "black", "on_red")
    if upload_speed < 15:
        speed_template["Speed_Up"] = colored(str(upload_speed) + " Mbps", "black", "on_red")
    else:
        speed_template["Speed_Down"] = str(download_speed) + "Mbps"
        speed_template["Speed_Up"] = str(upload_speed) + "Mbps"
    if results['ping'] > 50:
        speed_template["Speed_Latency"] = colored(str(round(results['ping'],1)) + " ms", "black", "on_red")
    else:
        speed_template["Speed_Latency"] = str(round(results['ping'],1)) + " ms"
    speed_template["Speed_URL"] = results_url
    return speed_template
