import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go


'''
app.layout =

set an html.Div to include Dropdown,
give an html.Div an id = id

update
output (div id, ?)
input (dropdown, value)

if dropdown_value == a:
    def (b)
    function
    x = x
    y = y

    return
     add_sliders
     add_graph(x,y)




'''
app = dash.Dash()

app.layout = html.Div([

    html.Div([
        dcc.Dropdown(
            value = ['m_1_3_2'],
            options = [{'label' : i, 'value' : i} for i in ['m_1_3_2','m_1_3_3','m_1_3_4','m_1_4_1','m_1_4_5','m_1_4_6','m_1_4_9','m_1_4_10','m_1_4_11']],
            multi=False,
            id='model_dropdown'
        )
    ]),

    html.Div([
        dcc.Graph(id='my_graph')
    ]),

    html.Div(id='slider_containter')
])




@app.callback(
    dash.dependencies.Output('slider_containter','children'),
    [dash.dependencies.Input('model_dropdown','value')])
def update_sliders(model_choice):

    def variable_slider(min,max,interval,variable_id,step):
        variable = np.arange(min,max,interval)
        return dcc.Slider(
            id=variable_id,
            min=variable.min(),
            max=variable.max(),
            value=variable.max(),
            step=step,
            marks={str(x): str(x) for x in np.unique(variable)})



    if model_choice == 'm_1_3_2':

        def m_1_3_2(a_dot):
            b_dot = a_dot
            return b_dot

        a_dot = np.arange(0,100,1)
        xplot = a_dot
        yplot = m_1_3_2(a_dot)

        return html.Div([
        html.Div(variable_slider(0,100000,10000,'L_slider',1), style = {'marginTop':30}),
        html.Div(variable_slider(0,20,2,'g_slider',1), style = {'marginTop':30})])



    elif model_choice == 'm_1_3_3':

        def m_1_3_3(beta,z,E):
            b_dot = beta*(z-E)
            return b_dot

        beta = 1
        z = 1000
        E = np.arange(0,1000,1)

        xplot = E
        yplot = m_1_3_3(beta, z, E)

        return html.Div([
        html.Div(variable_slider(0,100000,10000,'L_slider',1), style = {'marginTop':30}),
        html.Div(variable_slider(0,20,2,'g_slider',1), style = {'marginTop':30})])



@app.callback(
    dash.dependencies.Output('my_graph','figure'),
    [dash.dependencies.Input('model_dropdown','value')])
def update_graph(model_choice):

        if model_choice == 'm_1_3_2':

            def m_1_3_2(a_dot):
                b_dot = a_dot
                return b_dot

            a_dot = np.arange(0,100,1)
            xplot = a_dot
            yplot = m_1_3_2(a_dot)

            return {
        'data': [go.Scatter(
            x=xplot,
            y=yplot,
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'black'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': a_dot,
                'type': 'linear'
            },
            yaxis={
                'title': b_dot,
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }






if __name__ == '__main__':
    app.run_server(debug=True)


'''
Chapter 1
'''





def m_1_3_4(beta,z,Z_ro,a_dot):
    if z < Z_ro:
        b_dot = beta*(z-Z_ro)+a_dot
    elif z <= Z_ro:
        b_dot = a_dot
    return b_dot

def m_1_4_1(rho,g,H,delta_h,x,y):
    tao = rho*g*H*abs(delta_h(x,y))
    return tao

def m_1_4_5(sigma,dx,L):
    x = np.arange(0,(L/2)+dx,dx)
    h_afo_x = np.sqrt(sigma * x)
    return h_afo_x

def m_1_4_6(sigma,dx,L):
    x = np.arange(L/2,L+dx,dx)
    h_afo_x = np.sqrt(sigma * (L - x))
    return h_afo_x

def m_1_4_9(rho_i,rho_m):
    zeta = rho_i/(rho_m - rho_i)
    return zeta

def m_1_4_10(sigma,zeta,x):
    h_afo_x = np.sqrt((sigma/(1+zeta))*x)
    return h_afo_x

def m_1_4_11(sigma,zeta,x):
    h_afo_x = np.sqrt(sigma*(1+zeta)*x)
    return h_afo_x
