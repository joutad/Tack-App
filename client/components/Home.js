import { StyleSheet, View, Image, Text } from "react-native";
import React from "react";
import Logo from "../assets/images/logo.png";

const Home = () => {
  return (
    <View style={styles.root}>
      <Image source={Logo} style={styles.logo} resizeMode="contain" />
      <Text>Welcome to the</Text>
      <Text>Track App!</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    width: "100%",
    padding: 50,
  },
  logo: {
    width: "70%",
    maxWidth: 300,
    height: 100,
  },
});

export default SignInScreen;
