import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/zone")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <ul>
        {this.state.data.map(zoneTimes => {
          return (
            <li key={zoneTimes.user}>
              Couch Alotted: {zoneTimes.couch_alotted} Couch Used: {zoneTimes.couch_used} -
              Exercise Alotted: {zoneTimes.exercise_alotted} Exercise Used: {zoneTimes.exercise_used} -
              Creative Alotted: {zoneTimes.creative_allotted} Creative Used: {zoneTimes.creative_used} -
              Sleep Alotted: {zoneTimes.sleep_alotted} Sleep Used: {zoneTimes.sleep_used}
            </li>
          );
        })}
      </ul>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
