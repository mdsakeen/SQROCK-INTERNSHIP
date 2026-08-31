import argparse, re, json
from urllib.parse import urlparse

KEYWORDS={"login":15,"verify":15,"secure":10,"update":10,"account":15,"bank":15,"paypal":15}
def score(url):
    p=urlparse(url); score=0; reasons=[]
    if p.scheme!="https": score+=30; reasons.append("no_https")
    host=p.netloc.lower()
    for k,w in KEYWORDS.items():
        if k in host: score+=w; reasons.append(f"keyword:{k}")
    if host.count('.')>3: score+=25; reasons.append("many_subdomains")
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}",p.hostname or ""): score+=40; reasons.append("ip_hostname")
    return min(score,100),reasons

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("urls",nargs="*"); a=ap.parse_args()
    urls=a.urls or ["https://github.com","https://login.example.test/verify","http://192.0.2.10/login","https://secure.example.test/account","https://example.test/news","https://bank.example.test/update","https://portal.example.test","https://a.b.c.example.test/login","http://example.test","https://verify.example.test"]
    results=[]
    for u in urls:
        s,r=score(u); results.append({"url":u,"risk_score":s,"reasons":r}); print(f"{u} -> {s}%", ', '.join(r))
    open('output/phishing_scores.json','w').write(json.dumps(results,indent=2))
if __name__=="__main__": main()
