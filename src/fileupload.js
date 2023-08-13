import React, { useState } from 'react';
import axios from 'axios';
import Dropzone from 'react-dropzone';

function FileUploader() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleDrop = (acceptedFiles) => {
    setFile(acceptedFiles[0]);
  };

  const handleUpload = async () => {
    if (file) {
      console.log(file)
      const formData = new FormData();
      formData.append('file', file);
      
      try {
        const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });
        setMessage(response.data.message);
      } catch (error) {
        setMessage('Error uploading file.');
      }
    }
  };

  return (
    <div>
      <h1>Excel Upload</h1>
      <Dropzone onDrop={handleDrop}>
        {({ getRootProps, getInputProps }) => (
          <div {...getRootProps()} className="dropzone">
            <input {...getInputProps()} />
            <p>Drag and drop an Excel file here, or click to select a file</p>
          </div>
        )}
      </Dropzone>
      <button onClick={handleUpload} disabled={!file}>
        Upload
      </button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default FileUploader;

