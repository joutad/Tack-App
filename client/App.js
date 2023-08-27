import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";
import SignInScreen from "./components/SignInScreen";
import SignUpScreen from "./screens/SignUpScreen/SignUpScreen";
import ImageUploadForm from "./components/ImageUploadForm";

export default function App() {
  return (
    <View style={styles.container}>
      <SignInScreen />
      <ImageUploadForm />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#F9FBFC",
  },
});
