
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, dash_table, State
from app import app, server
from flask_login import logout_user, current_user
import login_page, error, page1, page2, profile, admin

navBar = dbc.Navbar(id='navBar',
    children=[],
    sticky='top',
    color='primary',
    className='navbar navbar-expand-lg navbar-dark bg-primary',
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        navBar,
        html.Div(id='pageContent')
    ])
], id='table-wrapper')


################################################################################
# HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
################################################################################
@app.callback(Output('pageContent', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/':
        if current_user.is_authenticated:
            return page1.layout
        else:
            return login_page.layout

    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return login_page.layout
        else:
            return login_page.layout

    if pathname == '/page1':
        if current_user.is_authenticated:
            return page1.layout
        else:
            return login_page.layout

    if pathname == '/page2':
        if current_user.is_authenticated:
            return page2.layout
        else:
            return login_page.layout

    if pathname == '/profile':
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login_page.layout

    if pathname == '/admin':
        if current_user.is_authenticated:
            if current_user.admin == 1:
                return admin.layout
            else:
                return error.layout
        else:
            return login_page.layout


    else:
        return error.layout


################################################################################
# ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
################################################################################
@app.callback(
    Output('navBar', 'children'),
    [Input('pageContent', 'children')])
def navBar(input1):
    if current_user.is_authenticated:
        if current_user.admin == 1:
            navBarContents = [
                dbc.NavItem(dbc.NavLink('Page 1', href='/page1')),
                dbc.NavItem(dbc.NavLink('Page 2', href='/page2')),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem('Admin', href='/admin'),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem('Logout', href='/logout'),
                    ],
                ),
            ]
            return navBarContents

        else:
            navBarContents = [
                dbc.NavItem(dbc.NavLink('Page 1', href='/page1')),
                dbc.NavItem(dbc.NavLink('Page 2', href='/page2')),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem('Logout', href='/logout'),
                    ],
                ),
            ]
            return navBarContents

    else:
        return ''



if __name__ == '__main__':
    app.title = 'مدیریت کاربران با فریمورک Dash'
    app.run_server(debug=False, port=1234)
