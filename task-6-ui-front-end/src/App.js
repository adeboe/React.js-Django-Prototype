/**
 * This governs the main point of entry for the entire front-end.
 *
 * Reference
 * https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
 *
 * @author Allan DeBoe
 * @date October 5th, 2022
 */
 
// Import Static Data
// import logo from './logo.svg';
import './App.css';

// Import JavaScript Libraries
import React from 'react';
import axios from 'axios';

// App
class App extends React.Component {
	
	// Used to store data from back-end
	state = {
		back_end_data : [],
	}
	
	// Used to get data from back-end
	componentDidMount() {
		
		let data;
		
		axios.get('http://localhost:8000/test/') // Our Django Web Server
		.then(response => {
			data = response.data;
			this.setState({
				back_end_data : data
			});
		})
		.catch(error => {})
		
	}
	
	// Renders a page for the user to see
	render() {
		return (
		//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		// HTML Here
		<div className="TestPage">
			<h1>SER401 - Task 6 (UI) Prototype</h1>
			<hr/>
				
			{this.state.back_end_data.map((data, id) => (
			<div key={id}>
				<h2>Name</h2>
				<p>{data.name}</p>
				<h2>General Information</h2>
				<p><b>Condition</b>: 			<i>{data.condition}</i></p>
				<p><b>Date Checked In</b>:		<i>{data.date_checked_in}</i></p>
				<p><b>Date Checked Out</b>:	<i>{data.date_checked_out}</i></p>
				<p><b>Location</b>:			<i>{data.location}</i></p>
				<p><b>Check Out By</b>:		<i>{data.check_out_by}</i></p>
				<h2>Description</h2>
				<p>{data.description}</p>
				<hr/>
			</div>
			))}
		</div>
		//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		);
	}
}

export default App;
