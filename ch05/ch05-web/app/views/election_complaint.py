from flask import current_app, jsonify, render_template, Response, request
import time
from app import redis_conn
from json import dumps

@current_app.route('/ch05/election/complaint/form', methods = ['GET','POST'])
async def create_complaint():
    if request.method == "GET":
        return render_template('complaint_form.html')
    else:
        voter_id = request.form['voter_id']
        complaint = request.form['complaint']
        record = {'voter_id': voter_id, 'complaint': complaint}
        redis_conn.publish("complaint_channel", dumps(record))
        return render_template('complaint_form.html')



@current_app.route('/ch05/elec/complaint/page')
async def post_election_complaint():
    return render_template('complaint_sse.html')

@current_app.route('/ch05/elec/comaplaint/stream')
async def elec_complaint_sse():
    def process_complaint_event():
        connection = redis_conn.pubsub()
        connection.subscribe('complaint_channel')
        for message in connection.listen():
            time.sleep(1)
            if message is not None and message['type'] == 'message':
                data = message['data']
                print(data)
            
                yield 'data: %s\n\n' % data
    return Response(process_complaint_event(), mimetype="text/event-stream")