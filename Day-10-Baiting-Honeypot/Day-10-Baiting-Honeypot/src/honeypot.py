from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import datetime, json
LOG_FILE='output/honeypot_log.jsonl'
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry={'time':datetime.datetime.now().isoformat(),'ip':self.client_address[0],'path':self.path,'agent':self.headers.get('User-Agent','?')}
        with open(LOG_FILE,'a',encoding='utf-8') as f: f.write(json.dumps(entry)+'\n')
        print(json.dumps(entry)); self.send_response(200); self.end_headers(); self.wfile.write(b'Lab honeypot: request logged.')
    def log_message(self,*args): pass
if __name__=='__main__':
    print('Honeypot running on http://127.0.0.1:8080'); ThreadingHTTPServer(('127.0.0.1',8080),Handler).serve_forever()
