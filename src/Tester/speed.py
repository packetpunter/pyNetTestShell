import speedtest
from TestUtils.TestObjects import TestResult

def speed_runner():
    ''' run speedtest '''
    tester = speedtest.Speedtest()
    speed_template = TestResult("speed").generate_frame()

    server = tester.get_best_server()
    tester.download()
    tester.upload()
    results_url = tester.results.share()
    results = tester.results.dict()
    speed_template["SRC"] = "self"
    speed_template["DST"] = server['sponsor'] + " " + server['name']
    speed_template["Speed_Down"] = str(round(results['download']/1024/1024, 0)) + " Mbps"
    speed_template["Speed_Up"] = str(round(results['upload']/1024/1024,0)) + " Mbps"
    speed_template["Speed_Latency"] = str(round(results['ping'],1)) + " ms"
    speed_template["Speed_URL"] = results_url
    return speed_template
