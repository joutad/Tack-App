import { StatusBar } from "expo-status-bar";
import { NativeAppEventEmitter, StyleSheet, Text, View } from "react-native";
import SignInScreen from "./screens/SignInScreen/SignInScreen";
import SignUpScreen from "./screens/SignUpScreen/SignUpScreen";
import ImageUploadForm from "./components/ImageUploadForm";
import Navigation from "./navigation/navigation";

export default function App() {
  return <Navigation />;
}

const styles = StyleSheet.create({
  // container: {
  //   flex: 1,
  //   backgroundColor: "#fff",
  //   alignItems: "center",
  //   justifyContent: "center",
  //   backgroundColor: "#F9FBFC",
  // },
});
