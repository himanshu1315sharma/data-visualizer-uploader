import React, { useState } from 'react';
import axios from 'axios';

const Data = () => {
  const [formData, setFormData] = useState({
    tableName: '',
    columns: '',
    values: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://localhost:5000/insert_data', formData)
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  };

  return (
    <div>
      <h1>Create Table and Insert Values</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Table Name:
          <input
            type="text"
            name="tableName"
            value={formData.tableName}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Columns (comma-separated):
          <input
            type="text"
            name="columns"
            value={formData.columns}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Values (comma-separated):
          <input
            type="text"
            name="values"
            value={formData.values}
            onChange={handleChange}
          />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Data;

