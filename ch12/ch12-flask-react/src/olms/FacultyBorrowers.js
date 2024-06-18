import React from 'react';

//export function PositionFunc(props){
export const FacultyBorrowers =(props)=>{
    const [id] = React.useState(0);
    const [firstname, setFirstname] = React.useState('');
    const [lastname, setLastname] = React.useState('');
    const [empid, setEmpid] = React.useState('');
    const [records, setRecords] = React.useState([]);
    
    React.useEffect(() => {
        const url_get = 'http://localhost:5000/fastapi/ch12/faculty/borrower/list/all';
        fetch(url_get)
        .then((response) =>  response.json() )
        .then((json) =>  { setRecords(json)})
        .catch((error) => console.log(error));
      }, []);

    const addRecord = () =>{
         const url_post = 'http://localhost:5000/fastapi/ch12/faculty/borrower/add';
         
         const options = {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                'id': id,
                'firstname': firstname,
                'lastname': lastname,
                'empid': empid
                }
            )

            
        }


         fetch(url_post, options)
            .then((response) => { response.json() })
            .then((json) => { console.log(json)})
            .catch((error) => console.log(error));

        
            const url_get = 'http://localhost:5000/fastapi/ch12/faculty/borrower/list/all';
            fetch(url_get)
            .then((response) =>  response.json() )
            .then((json) =>  { setRecords(json)})
            .catch((error) => console.log(error));
    }

    return <div>
           <form id='idForm1' onSubmit={ addRecord }>
               Employee ID: <input type='text' onChange={ (e) => { setEmpid(e.target.value)}} /><br/>
               First Name: <input type='text' onChange={ (e) => { setFirstname(e.target.value) }} /><br/>
               Last Name: <input type='text' onChange={ (e) => {setLastname(e.target.value)}}/><br/>
               <input type='submit' value='ADD Faculty Borrower' />
            </form>
            <br/>
            <h2>List of Faculty Borrowers</h2>
            <table >
				      <thead>
				        <tr>
				            <th>Id</th>
                            <th>Employee ID</th>
				            <th>First Name</th>
				            <th>Last Name</th>
				           
				        </tr>
				      </thead>

				      <tbody>
                {records.map((u) => (
                  <tr>
                    <td>{u.id}</td>
                    <td>{u.empid}</td>
                    <td>{u.firstname}</td>
                    <td>{u.lastname}</td>
                  
                  </tr>
                ))}
				      </tbody>
				    </table>
        </div>
}