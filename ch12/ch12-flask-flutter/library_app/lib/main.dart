import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:library_app/olms/provider/providers.dart';
import 'package:library_app/olms/tasks/task.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider.value(
        value: LoginProvider(),
      child: MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Packt Publishing (OLMS)',
      theme: ThemeData(
        primarySwatch: Colors.purple,
      ),
      home: const LoginHomePage(title: 'Library Management System'),
    )
    );
  }
}

class LoginHomePage extends StatefulWidget {
  const LoginHomePage({super.key, required this.title});
  final String title;

  @override
  State<LoginHomePage> createState() => LoginHomePageState();
}

class LoginHomePageState extends State<LoginHomePage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        title: Text(widget.title),
        centerTitle: true,
      ),
      body: const LoginViewWidget(),
    );
  }
}