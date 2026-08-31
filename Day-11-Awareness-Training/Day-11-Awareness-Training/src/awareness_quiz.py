import json
QUESTIONS=[
{"q":"An email asks for your password via a link. What is best?","opts":["A Click","B Verify with IT directly","C Reply"],"ans":"B","exp":"Use an official channel and never disclose passwords."},
{"q":"You find an unknown USB drive. What should you do?","opts":["A Plug it in","B Give it to security/IT","C Keep it"],"ans":"B","exp":"Unknown removable media can be a baiting vector."},
{"q":"A caller demands an MFA code. What should you do?","opts":["A Share it","B Refuse and verify independently","C Post it"],"ans":"B","exp":"MFA codes are sensitive authentication data."},
{"q":"Which is a phishing red flag?","opts":["A Unexpected urgency","B Known contact verified independently","C Routine meeting invite"],"ans":"A","exp":"Urgency is commonly used to pressure users."},
{"q":"A suspicious profile is very new with almost no posts. How should you treat it?","opts":["A Trust it","B Investigate cautiously","C Give it admin access"],"ans":"B","exp":"New, sparse profiles may require additional verification."},
{"q":"What is the safest way to open an unexpected account alert?","opts":["A Use the email link","B Navigate to the official site manually","C Forward it to strangers"],"ans":"B","exp":"Use known official routes rather than unexpected links."},
{"q":"What does MFA add?","opts":["A Another authentication factor","B Another username","C Public profile data"],"ans":"A","exp":"MFA requires more than one authentication factor."},
{"q":"What should you do after a suspected phishing click?","opts":["A Hide it","B Report promptly and follow incident guidance","C Share it"],"ans":"B","exp":"Rapid reporting can reduce impact."},
{"q":"What is vishing?","opts":["A Voice phishing","B Video compression","C DNS lookup"],"ans":"A","exp":"Vishing is voice-based phishing."},
{"q":"What is smishing?","opts":["A SMS phishing","B Secure hashing","C System imaging"],"ans":"A","exp":"Smishing uses SMS/text messages for phishing."}
]
score=0
for i,q in enumerate(QUESTIONS,1):
    print(f'\nQ{i}: {q["q"]}'); [print(o) for o in q['opts']]; ans=input('Answer: ').strip().upper()
    if ans==q['ans']: print('Correct'); score+=1
    else: print('Wrong -',q['exp'])
result={'score':score,'total':len(QUESTIONS),'percentage':round(score/len(QUESTIONS)*100,2)}
open('output/quiz_score.json','w').write(json.dumps(result,indent=2)); print(result)
