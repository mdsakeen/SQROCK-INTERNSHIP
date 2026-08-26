import argparse, json, re
from pathlib import Path
from urllib.parse import urlparse
import requests

PATTERN=re.compile(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}")

def fetch(url):
    p=urlparse(url)
    if p.scheme not in {"http","https"}: raise ValueError("Use HTTP/HTTPS")
    r=requests.get(url,timeout=10,headers={"User-Agent":"Sqrock-Day2-Lab/1.0"}); r.raise_for_status(); return r.text

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("--output",default="output/harvested_emails.json"); a=ap.parse_args()
    emails=sorted(set(x.lower() for x in PATTERN.findall(fetch(a.url))))
    out={"task":"Day 2","scope":"authorized lab only","source":a.url,"email_count":len(emails),"emails":emails}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(f"Found {len(emails)} email(s)"); [print(" -",e) for e in emails]; print("Saved:",a.output)
if __name__=="__main__": main()
