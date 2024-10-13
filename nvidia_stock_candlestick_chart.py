import pandas as pd
import plotly.graph_objects as go

# Loading the csv file
nvidia_stock = pd.read_csv('NvidiaStockPrice.csv')

# Ensure the 'Date' column is in datetime format
nvidia_stock['Date'] = pd.to_datetime(nvidia_stock['Date'])

# Filter the data to only show 2020 onwards
nvidia_stock_2020 = nvidia_stock[nvidia_stock['Date'] >= '2020-01-01']

# Create the candlestick chart 
candlestick_chart = go.Figure(data=[go.Candlestick(x=nvidia_stock_2020['Date'],
                open=nvidia_stock_2020['Open'],
                high=nvidia_stock_2020['High'],
                low=nvidia_stock_2020['Low'],
                close=nvidia_stock_2020['Close'],
                name='NVIDIA Stock Price',
                increasing_line_width=3,  
                decreasing_line_width=3)])  

# Key events on the chart with annotations
annotations = [
    dict(x='2020-09-13', 
         y=nvidia_stock_2020[nvidia_stock_2020['Date'] == '2020-09-01']['Close'].values[0] + 10, 
         xref='x', yref='y',
         text="ARM Acquisition Announced (Sep 13, 2020)", showarrow=True, arrowhead=2, ax=0, ay=-100),  # Even longer arrow
    
    dict(x='2021-07-19', 
         y=nvidia_stock_2020[nvidia_stock_2020['Date'] == '2021-07-01']['Close'].values[0] + 10, 
         xref='x', yref='y',
         text="Stock Split Announcement (Jul 19, 2021)", showarrow=True, arrowhead=2, ax=0, ay=-100),  # Even longer arrow
    
    dict(x='2022-02-07', 
         y=nvidia_stock_2020[nvidia_stock_2020['Date'] == '2022-02-01']['Close'].values[0] + 10, 
         xref='x', yref='y',
         text="ARM Deal Collapses (Feb 07, 2022)", showarrow=True, arrowhead=2, ax=0, ay=-100),  # Even longer arrow
    
    dict(x='2023-05-25', 
         y=nvidia_stock_2020[nvidia_stock_2020['Date'] == '2023-05-01']['Close'].values[0] + 10, 
         xref='x', yref='y',
         text="AI Boom & Earnings (May 25, 2023)", showarrow=True, arrowhead=2, ax=0, ay=-110)  # Even longer arrow
]

# Layout for minimal theme 
candlestick_chart.update_layout(
    title='NVIDIA Stock Price with Key Events (2020 onwards)',
    xaxis_title='Date',
    yaxis_title='Stock Price',
    xaxis_rangeslider_visible=False,  
    template='simple_white',  
    showlegend=False,  
    xaxis=dict(
        showline=True,  
        showgrid=False,  
        tickformat='%b %Y'  
    ),
    yaxis=dict(
        showline=True,  
        showgrid=False,  
        tickprefix='$', 
        showticklabels=True  
    ),
    annotations=annotations  
)

# Displaying the final chart
candlestick_chart.show()