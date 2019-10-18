import csv
import os.path

import bottle


class MurkleServer(object):
    # DANGER WILL ROBINSON!  We are using class variables
    # to store values accessed by the Bottle route functions
    # below.
    CSV_FH = None
    HTML_TEMPLATE = None
    
    def __init__(self, host, port, html_template, csv_file):
        self.host = host
        self.port = port
        MurkleServer.HTML_TEMPLATE = html_template
        MurkleServer.CSV_FILE = csv_file

    def serve(self):
        bottle.run(host=self.host, port=self.port)


@bottle.get('/')
def index():
    csv_fh = open(MurkleServer.CSV_FILE, 'r', encoding='utf-8')
    reader = csv.DictReader(csv_fh)
    total_tasks = len(list(reader))
    
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    template = open(os.path.join(templates_path, 'task-list.html'), 'r', encoding='utf-8').read()
    tpl = bottle.SimpleTemplate(template)
    return tpl.render(total_tasks=total_tasks)

@bottle.route('/task/<task_id>')
def task(task_id):
    csv_fh = open(MurkleServer.CSV_FILE, 'r', encoding='utf-8')
    reader = csv.DictReader(csv_fh)
    task_fields = list(reader)[int(task_id)]

    turk_template = open(MurkleServer.HTML_TEMPLATE, 'r', encoding='utf-8').read()

    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    template = open(os.path.join(templates_path, 'task_assignment_iframe.html'), 'r', encoding='utf-8').read()

    for field in task_fields.keys():
        turk_template = turk_template.replace(
            r'${' + field + r'}',
            task_fields[field]
        )

    tpl = bottle.SimpleTemplate(template)
    return tpl.render(turk_template=turk_template)

@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    return bottle.static_file(filepath, root=static_path)
