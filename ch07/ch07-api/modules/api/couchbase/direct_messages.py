
from flask import current_app, jsonify, request
from modules.repository.couchbase.direct_messages import DirectMessageRepository



@current_app.post('/chat/add')
def add_chats():
    data = request.get_json()
    repo = DirectMessageRepository() 
    result = repo.insert_dm(data)
    if result == False:
        return jsonify(message="error encountered in direct message record insert"), 500
    return jsonify(message="inserted direct message record"), 201

@current_app.patch('/chat/update')
def update_chats():
    data = request.get_json()
    repo = DirectMessageRepository() 
    result = repo.update_dm(data)
    if result == False:
        return jsonify(message="error encountered in direct message record update"), 500
    return jsonify(message="updated direct message record"), 201

@current_app.delete('/chat/delete/sender/<string:sender_id>')
def delete_chats_sender(sender_id:str):
    repo = DirectMessageRepository() 
    result = repo.delete_dm_sender(sender_id)
    if result == False:
        return jsonify(message="error encountered in direct message record delete"), 500
    return jsonify(message="deleted direct message record"), 201

# CREATE PRIMARY INDEX ON default:packtbucket.tfs.direct_messages;

@current_app.get('/chat/get/sender/<string:sender_id>')
def get_chat_sender(sender_id:str):
    repo = DirectMessageRepository() 
    records = repo.select_dm_sender(sender_id)
    return jsonify(records=records), 201


    
@current_app.get('/chat/list/all')
def list_all_chats():
    repo = DirectMessageRepository() 
    records = repo.select_all_dm()
    return jsonify(records=records), 201
    