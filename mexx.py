# example_form.py
from adminui import *

app = AdminApp()

#########################PARAMS#########################
app.app_title = 'Michelixx'

table_columns = [
    {'title': 'Rule Name', 'dataIndex': 'name'},
    {'title': 'Description', 'dataIndex': 'desc'},
    {'title': '# of Calls', 'dataIndex': 'callNo'},
    {'title': 'Status', 'dataIndex': 'status'},
    {'title': 'Updated At', 'dataIndex': 'updatedAt'}
]
table_data = [{
                "callNo": 76,
                "desc": "Description of Operation",
                "id": 0,
                "name": "Alpha",
                "status": 3,
                "updatedAt": "2019-12-13"
            }
            
]
#########################DATA#########################
def on_submit(form_data):
    print(form_data)



@app.login()
def on_login(username, password):
    if username=='alice' and password=='123456':
        return LoggedInUser("Alice")
    else:
        return LoginFailed()

def on_button_click():
    print('lol')

#Main Menu
app.set_menu(
    [
        MenuItem('Datasets', '/', icon="dashboard", children=[
            MenuItem('Machines', '/new', icon="info-circle"),
            MenuItem('Admin', '/admin', icon="setting"),
            #Button('Click Me', on_click=on_button_click)           
        ]),
        MenuItem('About', '/about', icon="info-circle")
    ])

@app.page('/', 'Machines')
def table_page():
    return [
        Card(content = [
            DataTable("Example Table", columns=table_columns,
                data=TableResult(table_data))])
    ]


if __name__ == '__main__':
    app.run()
