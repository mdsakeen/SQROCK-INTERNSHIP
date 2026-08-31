import json
from pathlib import Path
from datetime import datetime

MODULES={
'osint':'Run passive OSINT on a practice domain',
'profile':'Build profile from authorized public data',
'phish':'Score a URL for phishing indicators',
'template':'Generate awareness-training email',
'ir':'Trigger simulated incident response'
}

def run(module):
    if module not in MODULES: return {'status':'error','message':'Unknown module'}
    return {'status':'simulated','module':module,'description':MODULES[module]}

def full_chain():
    steps=[]
    for m in ['osint','profile','phish','template','ir']:
        steps.append(run(m))
    steps += [
      {'status':'simulated','module':'delivery','description':'Training delivery stage only; no email sent'},
      {'status':'simulated','module':'exploit','description':'No exploitation performed'},
      {'status':'simulated','module':'persist','description':'No persistence performed'}
    ]
    return {'timestamp':datetime.now().isoformat(),'simulation_only':True,'steps':steps}

def menu():
    print('\n=== SQROCK SE CHAIN SIMULATOR ===')
    for i,(k,v) in enumerate(MODULES.items(),1): print(f'[{i}] {k} - {v}')
    print('[6] full simulation')
    choice=input('Select: ').strip()
    names=list(MODULES)
    if choice=='6': result=full_chain()
    elif choice in {'1','2','3','4','5'}: result=run(names[int(choice)-1])
    else: result={'status':'error','message':'Invalid choice'}
    print(json.dumps(result,indent=2)); Path('output').mkdir(exist_ok=True); Path('output/final_simulation.json').write_text(json.dumps(result,indent=2))
if __name__=='__main__': menu()
