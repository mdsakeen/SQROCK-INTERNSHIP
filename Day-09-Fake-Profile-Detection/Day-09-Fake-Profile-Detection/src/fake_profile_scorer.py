import argparse, json
def score(p):
    score=0; reasons=[]
    age=p.get('account_age_days',365)
    if age<30: score+=30; reasons.append('new_account')
    ratio=p.get('following',0)/max(p.get('followers',1),1)
    if ratio>10: score+=25; reasons.append('high_following_ratio')
    if p.get('no_profile_pic'): score+=20; reasons.append('no_profile_picture')
    if p.get('posts',100)<5: score+=15; reasons.append('few_posts')
    if p.get('default_bio'): score+=10; reasons.append('default_bio')
    return min(score,100),reasons
if __name__=="__main__":
    samples=[
      {'id':'LAB-01','account_age_days':7,'followers':2,'following':900,'no_profile_pic':True,'posts':1,'default_bio':True},
      {'id':'LAB-02','account_age_days':1200,'followers':4500,'following':320,'no_profile_pic':False,'posts':870,'default_bio':False},
      {'id':'LAB-03','account_age_days':20,'followers':20,'following':500,'no_profile_pic':True,'posts':3,'default_bio':True},
      {'id':'LAB-04','account_age_days':600,'followers':800,'following':500,'no_profile_pic':False,'posts':150,'default_bio':False},
      {'id':'LAB-05','account_age_days':45,'followers':30,'following':400,'no_profile_pic':False,'posts':12,'default_bio':True}
    ]
    out=[]
    for p in samples:
        s,r=score(p); row={'profile_id':p['id'],'risk_score':s,'risk_level':'HIGH' if s>=70 else 'MEDIUM' if s>=40 else 'LOW','indicators':r}; out.append(row); print(p['id'],s,r)
    open('output/profile_scores.json','w').write(json.dumps(out,indent=2))
