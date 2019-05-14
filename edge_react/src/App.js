import React, { Component } from 'react';
import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import LandingPage from './components/Landing';
import Error from './components/Error';


export default class App extends Component {
  render() {
    return (
        <div className="">
        <BrowserRouter>
            <Switch>
                <Route exact path="/" component={LandingPage} />
                <Route component={Error} />
          </Switch>
          </BrowserRouter>
        </div>
    );
  }
}