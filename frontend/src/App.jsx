import { useState, useRef } from 'react';
import './App.css';

function App() {
  const fileInputRef = useRef(null);
  const API_URL = 'http://localhost:8000/api/upload/';
  const [responseData, setResponseData] = useState(null);


  // Inside your submitHandler function
  const handleSubmit = (e) => {
    e.preventDefault();
    const file = fileInputRef.current.files[0];
    if (file) {
      const formData = new FormData();
      formData.append('image', file);

      fetch(API_URL, {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log('Colors:', data);
          setResponseData(data); // Set the response data in state
        })
        .catch((error) => {
          console.error('Error:', error);
          // Handle the error
        });
    } else {
      console.log('No file selected.');
    }
  };

  return (
    <>
      <div className="form-container">
        <h1 className="heading">Image Uploading Form (Assignment)</h1>

        <form className="form" onSubmit={handleSubmit}>
          <div className="file" style={{ padding: '2px' }}>
            <input ref={fileInputRef} type="file" name="urineStrip" id="urineStrip" />
            <button type="submit">Submit</button>
          </div>

          <ul className="rules">
            <li>Image should be more than 2 MB</li>
            <li>Image should be visible properly to get accurate results</li>
          </ul>
        </form>
      </div>

      {responseData ? (
          <div className='result-container'>
            <p>
              {responseData}
            </p>
          </div>
        ):null}
    </>
  );
}

export default App;
