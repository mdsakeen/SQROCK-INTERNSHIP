import argparse

TEMPLATES={
"IT":("IT Support","Password-reset notification","Authority + fear","Verify through the official IT portal; never provide a password."),
"BANK":("Bank Security","Suspicious transaction alert","Authority + urgency","Call the bank using the number on the card/official website."),
"GOV":("Government Service","Account/document deadline","Authority + scarcity","Open the official government website directly; do not use unexpected links."),
}

def generate(kind):
    role,pretext,trigger,defense=TEMPLATES[kind]
    return f"""TRAINING SIMULATION - {kind}
Role: {role}
Pretext: {pretext}
Psychological trigger: {trigger}
Example opener: This is a controlled awareness scenario designed to demonstrate a social-engineering red flag.
Defensive response: {defense}
"""

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--type",choices=TEMPLATES.keys()); a=ap.parse_args()
    kinds=[a.type] if a.type else list(TEMPLATES)
    for k in kinds: print(generate(k)); print("-"*50)
