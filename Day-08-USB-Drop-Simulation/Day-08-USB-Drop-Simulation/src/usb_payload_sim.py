import argparse, datetime, json, os, platform, socket
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--output",default="output/usb_simulation.json"); a=ap.parse_args()
    info={"timestamp":datetime.datetime.now().isoformat(),"hostname":socket.gethostname(),"os":platform.system(),"version":platform.version(),"user":os.getenv("USERNAME") or os.getenv("USER"),"cwd":os.getcwd(),"simulation":True}
    open(a.output,'w').write(json.dumps(info,indent=2)); print('[SIM] Benign USB-drop payload executed'); print(json.dumps(info,indent=2))
