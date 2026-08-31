import argparse,datetime,json

def ir_response(incident):
    actions=[]
    sev=incident.get('severity','LOW').upper(); typ=incident.get('type','unknown')
    if sev in {'HIGH','CRITICAL'}: actions += ['SIMULATE_ACCOUNT_LOCK','SIMULATE_SESSION_REVOCATION','NOTIFY_SOC','PRESERVE_MAIL_LOGS']
    if typ=='phishing': actions += ['SIMULATE_EMAIL_QUARANTINE','SIMULATE_SENDER_BLOCK','SANDBOX_ATTACHMENT']
    report={'incident':incident,'actions':actions,'timestamp':datetime.datetime.now().isoformat(),'simulation_only':True}
    return report
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--type',default='phishing'); ap.add_argument('--severity',default='HIGH'); ap.add_argument('--user',default='lab-user@example.test'); a=ap.parse_args()
    r=ir_response({'type':a.type,'severity':a.severity,'user':a.user}); print(json.dumps(r,indent=2)); open('output/ir_report.json','w').write(json.dumps(r,indent=2))
