import json, requests, pprint
from flask import Flask, app, render_template, jsonify

def newTicket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {
        'username':'devnetuser',
        'password':'Cisco123!',
    }
    header = {
        'content-type':'application/json',
    }
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']

if __name__ == '__main__':
    ticket = newTicket()
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    urlHost = 'https://'+controller+'/api/v1/host'
    urlNet = 'https://'+controller+'/api/v1/network-device'
    urlTopology = 'https://'+controller+'/api/v1/topology/physical-topology'
    header = {
        'content-type':'application/json',
        'X-Auth-Token':ticket,
    }
    responseHost = requests.get(urlHost, headers=header, verify=False)
    responseNet = requests.get(urlNet, headers=header, verify=False)
    responseTopology = requests.get(urlTopology, headers=header, verify=False)

    print('Hosts = ')
    pprint.pprint(json.dumps(responseHost.json()['response']))

    print('Network = ')
    pprint.pprint(json.dumps(responseNet.json()['response']))

    print('Topology = ')
    pprint.pprint(json.dumps(responseTopology.json()['response']))

    app = Flask(__name__)

    @app.route('/menu')
    def menu():
        menu = '''
        <a href=\"/main\">Main</a><br>
        <br>
        <a href=\"/hosts\">Hosts</a><br>
        <a href=\"/network\">Network</a><br>
        <a href=\"/topology\">Topology</a><br>
        '''
        return render_template('base.html',content=menu,title='Menu')

    @app.route('/hosts')
    def hosts():
        content = json.dumps(responseHost.json()['response'])
        return render_template('base.html',content=content,title='Hosts')

    @app.route('/network')
    def network():
        content = json.dumps(responseNet.json()['response'])
        return render_template('base.html',content=content,title='Network')

    @app.route('/topology')
    def topology():
        content = json.dumps(responseTopology.json()['response'])
        return render_template('base.html',content=content,title='Topology')

    @app.route('/api/topology')
    def apiTopology():
        content = jsonify(responseTopology.json()['response'])
        return content

    @app.route('/')
    def main():
        return render_template('topology.html')

    app.run(debug=True)
