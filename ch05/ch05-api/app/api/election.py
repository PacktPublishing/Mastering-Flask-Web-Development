from flask import jsonify, current_app, request, make_response
from app.services.elections import check_election, approve_election, list_elections


@current_app.post('/ch05/election/verify')
async def verify_election():
    election_json = request.get_json()
    election_date = election_json['election_date']
    result_tuple = await check_election.send_async(current_app, election_date=election_date)
    isApproved = result_tuple[0][1]
    if isApproved:
        return jsonify(message=f'election for {election_date} is approved'), 201
    else:
        return jsonify(message=f'election for {election_date} is disabled'), 201

@current_app.post('/ch05/election/create')
async def create_election():
    election_json = request.get_json()
    result_tuple = await approve_election.send_async(current_app, details=election_json)
    isApproved = result_tuple[0][1]
    if isApproved:
        return jsonify(message=f'election for {election_json["election_date"]} created succesfully'), 201
    else:
        return jsonify(message=f'election for {election_json["election_date"]} failed'), 201

@current_app.get('/ch05/election/list/all')
async def list_all_election():
    records = await list_elections.send_async(current_app)
    return jsonify(record=records[0][1]), 201