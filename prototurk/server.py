
import csv
import json
import os.path

import bottle
from bs4 import BeautifulSoup


class ProtoTurkServer(object):
    # DANGER WILL ROBINSON!  We are using class variables
    # to store values accessed by the Bottle route functions
    # below.
    CSV_FH = None
    HTML_TEMPLATE = None
    
    def __init__(self, host, port, html_template, csv_file):
        self.host = host
        self.port = port
        ProtoTurkServer.HTML_TEMPLATE = html_template
        ProtoTurkServer.CSV_FILE = csv_file

    def serve(self):
        bottle.run(host=self.host, port=self.port)


@bottle.get('/')
def index():
    csv_fh = open(ProtoTurkServer.CSV_FILE, 'r', encoding='utf-8')
    reader = csv.DictReader(csv_fh)
    total_tasks = len(list(reader))

    bottle.response.add_header('Cache-Control', 'no-store')
    
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    template = open(os.path.join(templates_path, 'task-list.html'), 'r', encoding='utf-8').read()
    tpl = bottle.SimpleTemplate(template)
    return tpl.render(
        csv_filename=ProtoTurkServer.CSV_FILE,
        html_template_filename=ProtoTurkServer.HTML_TEMPLATE,
        total_tasks=total_tasks)

@bottle.route('/task/<ignore>.js.map')
def map_js_files(ignore):
    bottle.response.status = 404

@bottle.route('/task/<task_id>')
def task(task_id):
    csv_fh = open(ProtoTurkServer.CSV_FILE, 'r', encoding='utf-8')
    reader = csv.DictReader(csv_fh)
    tasks = list(reader)
    task_fields = tasks[int(task_id)]
    next_task_id = str((int(task_id) + 1) % len(tasks))

    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    template = open(os.path.join(templates_path, 'task_assignment.html'), 'r', encoding='utf-8').read()

    turk_template = open(ProtoTurkServer.HTML_TEMPLATE, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(turk_template, 'html.parser')
    turk_template_has_submit_button = bool(soup.select('input[type=submit]'))

    for field in task_fields.keys():
        turk_template = turk_template.replace(
            r'${' + field + r'}',
            task_fields[field]
        )

    bottle.response.add_header('Cache-Control', 'no-store')

    tpl = bottle.SimpleTemplate(template)
    return tpl.render(
        form_submit_url='/task/' + next_task_id,
        task_id=task_id,
        turk_template_has_submit_button=turk_template_has_submit_button,
        turk_template=turk_template)

@bottle.route('/task/<next_task_id>', method='post')
def task_submit(next_task_id):
    print('FORM DATA:')
    for key in bottle.request.forms:
        # Try to pretty print as JSON
        try:
            json_data = json.loads(bottle.request.forms[key])
            pretty_json = json.dumps(json_data, sort_keys=True, indent=2, separators=(',', ': '))
            print('  %s: %s' % (key, pretty_json))
        except (TypeError, json.decoder.JSONDecodeError):
            print('  %s: %s' % (key, bottle.request.forms[key]))
    bottle.redirect('/task/' + next_task_id)

@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    return bottle.static_file(filepath, root=static_path)
