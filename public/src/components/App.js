import React, { Component } from "react";
import { render } from "react-dom";

import Registration from "./auth/registration";

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
  }

  render() {
    return (
     <div>Hello
          <Registration />
     </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);