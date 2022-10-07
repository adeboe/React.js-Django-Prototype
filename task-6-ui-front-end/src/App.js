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
import logo from './logo.svg';
import './App.css';

// Import JavaScript Libraries
import React from 'react';
import axios from 'axios';

// App
class App extends React.Component {
	
	// Used to store data from back-end
	currentState = {
		back_end_data : [],
	}
	
	// Used to get data from back-end
	componentDidMount() {
		
		let data;
		
		axios.get('http://localhost:8000/react-test/') // Our Django Web Server
		.then(response => {
			data = response.data;
			this.setCurrentState({
				back_end_data : data;
			});
		})
		.catch(error => {})
		
	}
	
	// Renders a page for the user to see
	render() {
		return (
			//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			// HTML Here
			
			<div className="homepage">
				<h1>SER401 - Task 6 (UI) Prototype</h2>
				<hr>
				
				// Take data from back-end and display it.
				{this.currentState.back_end_data.map((data, id) => (
				
					<div key={id}>
						<h2>Condition</h2>
						<p>{data.condition}</p>
						<hr>
						<h2>Description</h2>
						<p>{data.description}</p>
						<hr>
					</div>
					
				)}

			</div>
			
			//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		);
	}
}

export default App;
