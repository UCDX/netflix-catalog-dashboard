from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Archivo en Drive, con ultima modificación: 2023-03-11 10:23 AM.
raw_data = pd.read_csv('netflix_movies_for_analitics.csv')

# ---------------------------------- Gráfico 1. Terminado ---------------------------------- #

df = raw_data.drop_duplicates(subset=['title'])
df_counts = df.groupby(['added_year', 'type']).size().reset_index(name='counts')
fig1 = px.bar(df_counts, x='added_year', y='counts', color='type', text_auto=True)

fig1.update_layout(
  title='Número de películas y series añadidas por año',
  xaxis_title='Año',
  yaxis_title='Cantidad',
  xaxis=dict(
    tickmode='linear'
  )
)

# ---------------------------------- Gráfico 2. PENDIENTE ---------------------------------- #

fig2 = fig1

# ---------------------------------- Gráfico 3. PENDIENTE ---------------------------------- #

fig3 = fig1

# ---------------------------------- Gráfico 4. PENDIENTE ---------------------------------- #

fig4 = fig1

# ---------------------------------- Dashboard ---------------------------------- #

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
  html.H1(
    children='Dashboard: Catálogo de películas y series en Netflix.',
    style={
      'textAlign': 'center'
    }
  ),

  # Fila 1. Gráficas 1 y 2.
  dbc.Row([
    dbc.Col(
      dcc.Graph(
        id='fig1',
        figure=fig1,
        style={
          'width': '90%',
          'margin': 'auto'
        }
      )
    ),
    dbc.Col( 
      dcc.Graph(
        id='fig2',
        figure=fig2,
        style={
          'width': '90%',
          'margin': 'auto'
        }
      )
    ) 
  ]),

  # Fila 2. Gráficas 3 y 4.
  dbc.Row([
    dbc.Col(
      dcc.Graph(
        id='fig3',
        figure=fig3,
        style={
          'width': '90%',
          'margin': 'auto'
        }
      )
    ),
    dbc.Col( 
      dcc.Graph(
        id='fig4',
        figure=fig4,
        style={
          'width': '90%',
          'margin': 'auto'
        }
      )
    ) 
  ])
])

if __name__ == '__main__':
  app.run_server(debug=True)
