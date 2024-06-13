from flask import  jsonify, render_template, Response
from modules.realtime import rt_bp
from  datetime import datetime
from json import loads, dumps
from asyncio import run

from sock_config import sock

@rt_bp.route('/ws/client/hpi/form', methods=['GET'])
async def render_ws_client_form():
    return render_template('hpi_ws_plot.html')

@sock.route('/ch06/ws/server/hpi/plot')
def ws_server_plot(ws):
    async def process():
        while True:
            hpi_data_json = ws.receive()
            hpi_data_dict = loads(hpi_data_json)
            print(hpi_data_dict)
            json_data = dumps(
                {'period': f"Y{hpi_data_dict['year']}Q{hpi_data_dict['quarter']}", 'hpi': float(hpi_data_dict['hpi'])})
            ws.send(json_data)
    run(process())
