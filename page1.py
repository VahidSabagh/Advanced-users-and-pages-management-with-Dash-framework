
# Dash packages
import dash_bootstrap_components as dbc
from dash import html
from app import app


###############################################################################
########### LANDING PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

        html.H2('Page 1 Layout'),
        html.Hr(),


], className="mt-4")
