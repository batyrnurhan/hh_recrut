import React, { Component } from "react";
import { Table } from "reactstrap";
import NewTeacherModal from "./NewTeacherModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal.js";

class TeacherList extends Component {
  render() {
    const teachers = this.props.teachers;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Document</th>
            <th>Phone</th>
            <th>Registration</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!teachers || teachers.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            teachers.map(teacher => (
              <tr key={teacher.pk}>
                <td>{teacher.name}</td>
                <td>{teacher.email}</td>
                <td>{teacher.document}</td>
                <td>{teacher.phone}</td>
                <td>{teacher.registrationDate}</td>
                <td align="center">
                  <NewTeacherModal
                    create={false}
                    teacher={teacher}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={teacher.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default TeacherList;