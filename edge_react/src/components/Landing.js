import React, { Component } from 'react';

class Landing extends Component {
    state = {
        objects: []
    }

    getObjects = async (e) => {
        e.preventDefault();
        try {
            const search_string = e.target.elements.search_string.value;
            const body = {
                "search_string": search_string
            }
            const api_call = await fetch(`http://localhost:80/search`, {
                method: 'POST',
                body: JSON.stringify(body),
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'PUT, GET, POST, DELETE, OPTIONS',
                    'Access-Control-Allow-Headers': 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
                }
            });
            const status = await api_call.status;
            console.log(status);
            if (status === 200) {
                const data = await api_call.json();
                this.setState({
                    objects: data
                });
                console.log(data);
            }
            else {
                console.log('could not get objects');
                alert('could not get objects');
            }
        }
        catch (err) {
            console.log(err);
            alert('data server is not responding');
        }

    }

    render() {
        return (
            <div className="container">
                <div className="header-logo">
                </div>
                <div className="header">
                </div>
                <div className="main-landing">
                    <br></br>
                    <form onSubmit={this.getObjects}>
                        <input type="text" name="search_string" placeholder="Search String(comma seperated)"></input><br></br><br></br>
                        <button>Get Objects</button>
                    </form><br></br>
                    {this.state.objects && this.state.objects.map((object) => {
                        return (
                                <div className="body-item">  
                                    <div key = {object.productId}>
                                        <p >product/productId : {object.productId}</p>
                                        <p >review/userId: {object.userId}</p>
                                        <p >review/profileName: {object.profileName}</p>
                                        <p >review/helpfulness: {object.helpfulness}</p>
                                        <p >review/score : {object.score}</p>
                                        <p >review/time: {object.time}</p>
                                        <p >review/summary: {object.summary}</p>
                                        <p >review/text: {object.text}</p>                                        
                                    </div> <br/>
                                </div>
                            );
                        })} 
                </div>
                <div className="footer">
                </div>
            </div>
        )
    }
}

export default Landing;