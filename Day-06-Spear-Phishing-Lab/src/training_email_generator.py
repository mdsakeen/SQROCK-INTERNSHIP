import argparse, json

def training_email(target):
    name=target["name"]; company=target["company"]; location=target.get("location","")
    return f"""[SECURITY AWARENESS TRAINING - LAB ONLY]
From: awareness@lab.internal
To: {target["email"]}
Subject: Action Required - Training Scenario

Hi {name},

This is a controlled training scenario for {company}. A simulated account-alert pretext is being used to demonstrate how urgency and personalization can influence users.
Location clue used in scenario: {location}

[TRAINING LINK: https://lab.internal/awareness-test]

Defender reminder: verify unexpected requests through official channels.
"""

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--output",default="output/training_emails.json"); a=ap.parse_args()
    targets=[{"name":"Riya Sharma","email":"riya@example.test","company":"Example Lab","location":"Lab"},{"name":"Arun Kumar","email":"arun@example.test","company":"Example Lab","location":"Lab"},{"name":"Sara Ali","email":"sara@example.test","company":"Example Lab","location":"Lab"}]
    out=[{"target":t,"email":training_email(t)} for t in targets]
    open(a.output,'w').write(json.dumps(out,indent=2)); print(f"Generated {len(out)} awareness-training drafts")
