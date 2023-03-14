from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Archivo en Drive, con ultima modificación: 2023-03-11 10:23 AM.
raw_data = pd.read_csv('netflix_movies_for_analitics.csv')

# ---------------------------------- Gráfico 1. ---------------------------------- #

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

# ---------------------------------- Gráfico 2. ---------------------------------- #

df_f2 = df
conteo1 = df_f2['rating'].value_counts()
fig2_1 = px.pie(names=conteo1.index, values=conteo1.values)
fig2_1.update_layout(
  title='Rating de series y películas'
)

df_f2['rating'] = df_f2['rating'].replace({
    'TV-PG': 'Niños[TV-PG,PG,TV-G,TV-Y7,TV-Y,G,TV-Y7-FV]',
    'PG': 'Niños[TV-PG,PG,TV-G,TV-Y7,TV-Y,G,TV-Y7-FV]',
    'TV-G': 'Niños[TV-PG,PG,TV-G,TV-Y7,TV-Y,G,TV-Y7-FV]',
    'TV-Y7': 'Niños[TV-PG,PG,TV-G,TV-Y7,TV-Y,G,TV-Y7-FV]',
    'TV-Y': 'Niños[TV-PG,PG,TV-G,TV-Y7,TV-Y,G,TV-Y7-FV]',
    'G': 'Niños[TV-PG,PG,TV-G,TV-Y7,TV-Y,G,TV-Y7-FV]',
    'TV-Y7-FV': 'Niños[TV-PG,PG,TV-G,TV-Y7,TV-Y,G,TV-Y7-FV]', 
    'TV-14': 'Adolescentes[TV-14,PG-13]',
    'PG-13': 'Adolescentes[TV-14,PG-13]',
    'TV-MA': 'Adultos[TV-MA,R,NC-17]',
    'R': 'Adultos[TV-MA,R,NC-17]',
    'NC-17': 'Adultos[TV-MA,R,NC-17]',
    'NR':'Sin clasificar[NR,UR]',
    'UR':'Sin clasificar[NR,UR]'
    })

conteo2 = df_f2['rating'].value_counts()
fig2_2 = px.pie(names=conteo2.index, values=conteo2.values)
fig2_2.update_layout(
  title='Rating por público específico'
)

# ---------------------------------- Gráfico 3. ---------------------------------- #

df_f3 = df
df_counts_fig3 = df.groupby(['country', 'type']).size().reset_index(name='counts')
df_counts_fig3 = df_counts_fig3.groupby('type').apply(lambda x: x.nlargest(10, 'counts')).reset_index(drop=True)
fig3 = px.bar(df_counts_fig3, x= 'country', y = 'counts', color = 'type', text_auto = True)
fig3.update_layout(
    title = 'Número de peliculas y series añanidas por país',
    xaxis_title = 'País',
    yaxis_title = 'Cantidad',
    xaxis=dict(
        tickmode='linear'
    )
)

# ---------------------------------- Gráfico 4. ---------------------------------- #

df_f4 = df

df_f4['type'] = df_f4['type'].replace({
  'Movie': 'Movie (minutes)',
  'TV Show': 'TV Show (Seasons)'
})
fig4 = px.histogram(df_f4, x='duration_value', color='type')
fig4.update_layout(
  title='Frecuencia de duración de una película o serie',
  xaxis_title='Duración',
  yaxis_title='Frecuencia'
)

# ---------------------------------- Dashboard ---------------------------------- #

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
  html.H1(
    children='Dashboard: Catálogo de películas y series en Netflix.',
    style={
      'textAlign': 'center'
    }
  ),

  # Fila 1. Gráfica 1.
  dbc.Row([
    dbc.Col(
      dcc.Graph(
        id='fig1',
        figure=fig1,
        style={
          'width': '100%',
          'margin': 'auto'
        }
      )
    )
  ]),
  # Fila 2. Gráfica 2-1 y 2-2.
  dbc.Row([
    dbc.Col(
      dcc.Graph(
        id='fig2_1',
        figure=fig2_1,
        style={
          'width': '90%',
          'margin': 'auto'
        }
      )
    ),
    dbc.Col(
      dcc.Graph(
        id='fig2_2',
        figure=fig2_2,
        style={
          'width': '90%',
          'margin': 'auto'
        }
      )
    )
  ]),

  # Fila 3. Gráficas 3 y 4.
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
