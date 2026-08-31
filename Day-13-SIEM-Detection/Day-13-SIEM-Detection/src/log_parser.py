import re, json
from collections import Counter
from datetime import datetime
LOG_SAMPLE='2024-01-15 02:34:12 FAILED_LOGIN user=admin ip=45.33.32.156\n2024-01-15 02:34:14 FAILED_LOGIN user=admin ip=45.33.32.156\n2024-01-15 02:34:16 FAILED_LOGIN user=admin ip=45.33.32.156\n2024-01-15 02:34:18 SUCCESS_LOGIN user=admin ip=45.33.32.156\n2024-01-15 08:00:01 SUCCESS_LOGIN user=lab-user ip=192.168.1.10\n2024-01-15 02:35:00 EMAIL_RULE_CREATED user=admin rule=forward_all\n'

def analyze(logs):
    fails=re.findall(r'FAILED_LOGIN user=(\w+) ip=([\d.]+)',logs); rules=re.findall(r'EMAIL_RULE_CREATED user=(\w+)',logs); alerts=[]
    counts=Counter(u for u,_ in fails)
    for user,count in counts.items():
        if count>=3: alerts.append({'type':'BRUTE_FORCE','user':user,'count':count,'severity':'HIGH'})
    for user in rules: alerts.append({'type':'SUSPICIOUS_EMAIL_RULE','user':user,'severity':'HIGH'})
    return alerts
if __name__=='__main__':
    alerts=analyze(LOG_SAMPLE); [print('[ALERT]',a) for a in alerts]; open('output/alerts.json','w').write(json.dumps(alerts,indent=2))
