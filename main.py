import requests, os, ctypes, time, threading, httpx

start = time.time()
os.system("cls")

total = 0 
success = 0
failed = 0
f = open("proxies.txt", "r").readlines()
ips = len(f)

def GetFormattedProxy(proxy):
    if '@' in proxy:
        return proxy
    elif len(proxy.split(':')) == 2:
        return proxy
    else:
        if '.' in proxy.split(':')[0]:
            return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
        else:
            return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])
def update():
    global total, success, failed, ips
    speed = round(total / ((time.time() - start) / 60))
    ctypes.windll.kernel32.SetConsoleTitleW("[ipv4.games] | Total Requests: %s | Success: %s | Failed: %s | IPs: %s | R/S: %s" % (total, success, failed, ips, speed))

def claim():
    try:
        global total, success, failed
        total += 1
        update()
        proxy = GetFormattedProxy("161.129.152.226:42277")
        # proxy = {'http': "161.129.152.226:42277"}
        # proxy = {'http': 'http://%s' % ip}
        client = httpx.Client(timeout=3, proxies={"all://": f"http://{proxy}"})
        r = client.get("https://ipv4.games/claim?name=exploit")
        idk = r.text.split("\n")
        idk = idk[1].replace("<title>", "").replace("</title>", "")
        print("[+]", idk)
        if r.status_code in (200, 201, 204):
            success += 1
            update()
        else:
            print("[-]", "Failed to claim", r.status_code)
            failed += 1
            update()
    except Exception as e:
        failed += 1
        update()
        print("[-]", "Failed to claim", e)

for idk in range(69999):
    threading.Thread(target=claim).start()
    
