import React, { useState } from "react";
import { View, Text, Pressable, Image, StyleSheet } from "react-native";
import * as ImagePicker from "expo-image-picker";
import axios from "axios";

const ImageUploadForm = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [predictionText, setPredictionText] = useState("");

  const handleImageChange = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    console.log(result);

    if (!result.canceled) {
      setSelectedImage(result.assets[0].uri);
    }
  };

  const handleImageUpload = async () => {
    const formData = new FormData();
    formData.append("image", {
      uri: selectedImage,
      type: "image/jpeg", // or 'image/png'
      name: "image.jpg", // or 'image.png'
    });

    try {
      const response = {
        data: {
          prediction_text: "key"
        }
      };
      /*await axios.post("/members", formData, { //Axios and React-Native are not working properly, even though the same code worked in React
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });*/
      const { prediction_text } = response.data;
      console.log(prediction_text);
      setPredictionText(prediction_text);
    } catch (error) {
      console.error("Error uploading image:", error);
    }
  };

  return (
    <View>
      <Pressable style={styles.button} onPress={handleImageChange}>
        <Text>Select Image</Text>
      </Pressable>
      {selectedImage && (
        <>
          <Image
            source={{ uri: selectedImage }}
            style={{ width: 100, height: 100 }}
          />
          <Pressable style={styles.button} onPress={handleImageUpload}>
            <Text>Upload Image</Text>
          </Pressable>
        </>
      )}
      <Text>{predictionText}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  button: {
    alignItems: "center",
    justifyContent: "center",
    padding: 10,
    backgroundColor: "#e0e0e0",
    margin: 5,
    borderRadius: 5,
  },
});

export default ImageUploadForm;
