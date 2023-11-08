import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, dash_table, State
from app import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlLogin', refresh=True),
        html.Div([
            dbc.Container(
                html.Img(
                    src='/assets/dash-logo-stripe.JPG',
                    className='center'
                ),
            ),
            html.Br(),
            dbc.Container(id='loginType', children=[
                dcc.Input(
                    placeholder='Username',
                    type='text',
                    id='usernameBox',
                    className='form-control',
                    n_submit=0,
                    style={'width': '400px'}
                ),
                html.Br(),
                dcc.Input(
                    placeholder='Password',
                    type='password',
                    id='passwordBox',
                    className='form-control',
                    n_submit=0,
                    style={'width': '400px'}
                ),
                html.Br(),
                html.Button(
                    children='Login',
                    n_clicks=0,
                    type='submit',
                    id='loginButton',
                    className='btn btn-primary btn-lg'
                    , style={'margin-bottom': '10px'}
                ),
                html.Br(),
            ], className='form-group', style={'margin-left': '260px'}),
        ], style={"background-color": "#e2e5fd", }),
    ])
])


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - REDIRECT TO PAGE1 IF LOGIN DETAILS ARE CORRECT
################################################################################
@app.callback(Output('urlLogin', 'pathname'),
              [Input('loginButton', 'n_clicks'),
               Input('usernameBox', 'n_submit'),
               Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def sucess(n_clicks, usernameSubmit, passwordSubmit, username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            return '/page1'
        else:
            pass
    else:
        pass


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('usernameBox', 'className'),
              [Input('loginButton', 'n_clicks'),
               Input('usernameBox', 'n_submit'),
               Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('passwordBox', 'className'),
              [Input('loginButton', 'n_clicks'),
               Input('usernameBox', 'n_submit'),
               Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'
