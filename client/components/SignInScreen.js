import {
  StyleSheet,
  View,
  Image,
  Text,
  useWindowDimensions,
} from "react-native";
import React from "react";
import Logo from "../assets/images/logo.png";

const SignInScreen = () => {
  const { height } = useWindowDimensions();
  return (
    <View style={styles.root}>
      <Image
        source={Logo}
        style={[styles.logo, { height: height * 0.3 }]}
        resizeMode="contain"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    flex: 1,
    alignItems: "center",
    width: "100%",
    padding: 50,
  },
  logo: {
    width: "70%",
    maxWidth: 300,
    maxHeight: 200,
    height: 100,
  },
});

export default SignInScreen;
