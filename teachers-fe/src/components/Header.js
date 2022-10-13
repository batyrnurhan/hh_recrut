import React, { Component } from "react";
import {
  createBrowserRouter,
  RouterProvider,
  Route,
} from "react-router-dom";

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
        <h5>
          <i>Creating a web platform for the higher education ecosystem</i>
        </h5>
        <hr />
        <h1>Teacher's list</h1>

        {/* ??? ??? ?????? ?????? */}
        <div>
          <a className="login_as_teacher" href="/login_teacher"><h1>Login as teacher</h1></a>
        </div>
        <div>
          <a className="login_as_university" href="/login_university"><h1>Login as university</h1></a>
        </div>
        <div>
          <a className="login_as_staff" href="/login_staff"><h1>Login as staff</h1></a>
        </div>

      </div>
    );
  }
}

export default Header;