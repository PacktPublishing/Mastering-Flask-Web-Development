import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:library_app/olms/models/login.dart';

class LoginProvider with ChangeNotifier{
  List<Login> _items = [];
  

  List<Login> get items {
    return [..._items];
  }

  Future<void> addLogin(String username, String password, String role ) async {
    String url = 'http://172.21.160.1:5000/login/add';
    try{
      if(username.isEmpty || password.isEmpty || role.isEmpty){
         return;
      }
      Map<String, dynamic> request = {"username": username, "password": password, "role": int.parse(role)};
      final headers = {'Content-Type': 'application/json'};
      final response = await http.post(Uri.parse(url), headers: headers, body: json.encode(request));
      Map<String, dynamic> responsePayload = json.decode(response.body);
      final login = Login(
          username: responsePayload["username"],
          password: responsePayload["password"],
          role: responsePayload["role"]
      );
      print(login);
      notifyListeners();
    }catch(e){
      print(e);
    }
      

    
  }


  Future<void> get getLogin async {
    String url = 'http://172.21.160.1:5000/login/list/all';
    var response;
    try{
      response = await http.get(Uri.parse(url));
      Map body = json.decode(response.body);
      
      List<Map> loginRecs = body["records"].cast<Map>();
      print(loginRecs);
      _items = loginRecs.map((e) => Login(
          id: e["id"],
          username: e["username"],
          password: e["password"],
          role: e["role"],
      )
      ).toList();
      
    }catch(e){
      print(e);
    }

    notifyListeners();
  }

}