import { useState, useEffect } from 'react';
import './App.css';
import ImageUploadForm from './components/ImageUploadForm';

function App() {

  const [data, setData] = useState([{}])

    // useEffect(() => {
    //   fetch('/members').then(
    //     res => res.json()
    //   ).then(
    //     data => {
    //         setData(data)
    //         console.log(data)
    //     } 
    //   )
    // }, []);

  return (
    <div>

      {/* {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ): (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )} */}

      <h1>Image Upload Form</h1>
      <ImageUploadForm />

    </div>
  );
}

export default App;
