# securex_ise.py

from flask import Flask, request, Response
import sys
sys.path.append('pxgrid-rest-ws/python')
import time
from pxgrid import PxgridControl
from config import Config
from anc_query_all import queryANC
import json

app = Flask(__name__)

@app.route('/api/ise/updatehost', methods=['POST'])
def updatehost():
  data = json.loads(request.data)
  print(json.dumps(data, indent=4, sort_keys=True))
  return "{}"

@app.route('/api/ise/blockToggle', methods=['POST'])
def blockToggle():
  data = json.loads(request.data)
  print(json.dumps(data, indent=4, sort_keys=True))
  url = service['properties']['restBaseUrl'] + '/applyEndpointBy' + data["action"]
  resp = queryANC(config, secret, url, '{"policyName":"QUARANTINE","%s":"%s"}' % (data["action"][0].lower() + data["action"][1:], data["target"]))
  data = json.loads(resp["body"])
  if "failureReason" in data and data["failureReason"]=="mac address is already associated with this policy":
    url = service['properties']['restBaseUrl'] + '/clearEndpointByMacAddress'
    resp = queryANC(config, secret, url, '{"macAddress":"%s"}' % data["macAddress"])
  return Response(resp["body"], status=resp["code"], mimetype='application/json')

if __name__ == '__main__':
    config = Config()
    pxgrid = PxgridControl(config=config)

    while pxgrid.account_activate()['accountState'] != 'ENABLED':
        time.sleep(60)
    # lookup for session service
    service_lookup_response = pxgrid.service_lookup('com.cisco.ise.config.anc')
    service = service_lookup_response['services'][0]
    node_name = service['nodeName']
    secret = pxgrid.get_access_secret(node_name)['secret']
    app.run(debug=True)
