import React, { useState } from 'react';
import axios from 'axios';

const ImageUploadForm = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [predictionText, setPredictionText] = useState('');

    const handleImageChange = (event) => {
        setSelectedImage(event.target.files[0]);
    };

    const handleImageUpload = async () => {
        const formData = new FormData();
        formData.append('image', selectedImage);

        try {
            const response = await axios.post('/members', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            // Handle success or update UI
            let { prediction_text } = response.data;
            // prediction_text = prediction_text.substring(0, prediction_text.indexOf(':'));
            console.log(prediction_text);
            setPredictionText(prediction_text);
        }
        catch (error) {
            console.error('Error uploading image:', error);
        }
    };

    return (
        <div>
            <input type="file" accept="image/*" onChange={handleImageChange} />
            <button onClick={handleImageUpload}>Upload Image</button>
            <p>{predictionText}</p>
        </div>
    );
};

export default ImageUploadForm;
