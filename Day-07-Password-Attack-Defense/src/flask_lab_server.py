from flask import Flask, request, jsonify
from time import monotonic
from collections import defaultdict
app=Flask(__name__)
ATTEMPTS=defaultdict(list)
LAB_USER={"username":"admin","password":"LabOnly-123!"}
WINDOW=30; LIMIT=5
@app.post("/login")
def login():
    key=request.remote_addr
    now=monotonic(); ATTEMPTS[key]=[t for t in ATTEMPTS[key] if now-t<WINDOW]
    if len(ATTEMPTS[key])>=LIMIT: return jsonify({"status":"rate_limited"}),429
    ATTEMPTS[key].append(now)
    data=request.get_json(silent=True) or request.form
    if data.get("username")==LAB_USER["username"] and data.get("password")==LAB_USER["password"]: return jsonify({"status":"welcome"}),200
    return jsonify({"status":"invalid"}),401
if __name__=="__main__": app.run(host="127.0.0.1",port=5000)
