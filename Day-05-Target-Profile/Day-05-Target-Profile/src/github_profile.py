import argparse, json, requests

def fetch_json(url):
    r=requests.get(url,headers={"Accept":"application/vnd.github+json","User-Agent":"Sqrock-Day5-Lab/1.0"},timeout=10); r.raise_for_status(); return r.json()

def profile(username):
    u=fetch_json(f"https://api.github.com/users/{username}")
    repos=fetch_json(f"https://api.github.com/users/{username}/repos?per_page=100")
    langs={}
    for r in repos:
        if r.get("language"): langs[r["language"]]=langs.get(r["language"],0)+1
    return {"username":username,"name":u.get("name"),"company":u.get("company"),"location":u.get("location"),"public_repos":u.get("public_repos"),"bio":u.get("bio"),"top_languages":dict(sorted(langs.items(),key=lambda x:-x[1])[:10])}

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("username"); ap.add_argument("--output",default="output/target_profile.json"); a=ap.parse_args()
    p=profile(a.username); open(a.output,'w').write(json.dumps(p,indent=2)); print(json.dumps(p,indent=2))
