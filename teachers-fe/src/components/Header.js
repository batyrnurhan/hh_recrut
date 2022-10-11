import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="https://cdn.worldvectorlogo.com/logos/shrek.svg"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <div align="right"><button>Login</button></div>
        <h5>
          <i>Creating a web platform for the higher education ecosystem</i>
        </h5>
        <hr />
        <h1>Teacher's list</h1>
      </div>
    );
  }
}

export default Header;