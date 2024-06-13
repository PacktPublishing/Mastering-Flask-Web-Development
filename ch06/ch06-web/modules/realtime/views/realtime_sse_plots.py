from modules.realtime import rt_bp
from redis_config import redis_conn
from flask import render_template, request, Response
from json import loads, dumps
from  datetime import datetime

@rt_bp.route('/sse/client/hpi/form', methods = ['GET','POST'])
async def create_complaint():
    if request.method == "GET":
        return render_template('hpi_sse_plot_form.html')
    else:
        hpi = request.form['hpi']
        year = request.form['year']
        quarter = request.form['quarter']
        json_data = dumps(
                {'period': f"Y{year}Q{quarter}", 'hpi': float(hpi)})
        redis_conn.publish("data_channel", json_data)
        return render_template('hpi_sse_plot_form.html')

@rt_bp.route('/sse/client/result/plot')
async def post_election_complaint():
    return render_template('hpi_sse_plot.html')

@rt_bp.route('/sse/hpi/data/stream')
async def elec_complaint_sse():
    def process_complaint_event():
        connection = redis_conn.pubsub()
        connection.subscribe('data_channel')
        for message in connection.listen():
           
            if message is not None and message['type'] == 'message':
                data = message['data']
                print(data)
            
                yield f"data:{data}\n\n"
    return Response(process_complaint_event(), mimetype="text/event-stream")