import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:library_app/olms/provider/providers.dart';


class LoginViewWidget extends StatefulWidget {
  const LoginViewWidget({Key? key}) : super(key: key);

  @override
  State<LoginViewWidget> createState() => _TasksWidgetState();
}

class _TasksWidgetState extends State<LoginViewWidget> {
  TextEditingController userNameController = TextEditingController();
  TextEditingController passwordController = TextEditingController();
  TextEditingController roleController = TextEditingController();
 
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              Expanded(
                child: TextFormField(
                  controller: userNameController,
                  decoration: const InputDecoration(
                    labelText: 'Username',
                    border: OutlineInputBorder(),
                  ),
                ),
              ),
              Expanded(
                child: TextFormField(
                  controller: passwordController,
                  decoration: const InputDecoration(
                    labelText: 'Password',
                    border: OutlineInputBorder(),
                  ),
                ),
              ),
              Expanded(
                child: TextFormField(
                  controller: roleController,
                  decoration: const InputDecoration(
                    labelText: 'Role',
                    border: OutlineInputBorder(),
                  ),
                ),
              ),
             
              const SizedBox(width: 10,),
              ElevatedButton(
                  style: ButtonStyle(
                      backgroundColor: MaterialStateProperty.all(Colors.amberAccent),
                      foregroundColor: MaterialStateProperty.all(Colors.purple)
                  ),
                  child: const Text("Add"),
                  onPressed: () {
                    Provider.of<LoginProvider>(context, listen: false).addLogin(userNameController.text, passwordController.text, roleController.text);
                    userNameController.clear();
                    passwordController.clear();
                    roleController.clear();
                   
                  }
              )
            ],
          ),
          FutureBuilder(
            future: Provider.of<LoginProvider>(context, listen: false).getLogin,
            builder: (ctx, snapshot) =>
            snapshot.connectionState == ConnectionState.waiting
                ? const Center(child: CircularProgressIndicator())

                :
            Consumer<LoginProvider>(
              child: Center(
                heightFactor: MediaQuery.of(context).size.height * 0.03,
                child: const Text('You have no tasks.', style: TextStyle(fontSize: 18),),
              ),
              builder: (ctx, loginProvider, child) => loginProvider.items.isEmpty
                  ?  child as Widget
                  : Padding(
                padding: const EdgeInsets.only(top: 20),
                child:  Container(
                  height: MediaQuery.of(context).size.height * 0.6,
                  child: ListView.builder(
                      itemCount: loginProvider.items.length,
                      itemBuilder: (ctx, i) =>  Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        const SizedBox(
                          height: 12.0,
                          width: 20.2,
                        ),
                        Container(
                          decoration: BoxDecoration(
                            color: Color.fromARGB(255, 204, 218, 127),
                            borderRadius: const BorderRadius.all(
                              Radius.circular(12.0),
                            ),
                          ),
                          child: SingleChildScrollView(
                            scrollDirection: Axis.horizontal,
                            child: DataTable(
                              columns: <DataColumn>[
                                 DataColumn(
                                  label: Text(
                                    'Username',
                                    style:
                                        TextStyle(fontStyle: FontStyle.italic),
                                  ),
                                ),
                                DataColumn(
                                  label: Text(
                                    'Password',
                                    style:
                                        TextStyle(fontStyle: FontStyle.italic),
                                  ),
                                ),
                                DataColumn(
                                  label: Text(
                                    'Role',
                                    style:
                                        TextStyle(fontStyle: FontStyle.italic),
                                  ),
                                ),
                              ],
                              rows: <DataRow>[
                                DataRow(
                                  cells: <DataCell>[
                                    DataCell(
                                        Text(loginProvider.items[i].username)),
                                    DataCell(
                                        Text(loginProvider.items[i].password)),
                                    DataCell(Text(loginProvider.items[i].role.toString())),
                                  ],
                                ),
                              ],
                            ),
                          ),
                        ),
                       const SizedBox(
                          height: 16.0,
                        ),
                      ],
                    )
                  ),
                ),
              ),
            ),
          )
          
        ],
      ),
    );
  }
}