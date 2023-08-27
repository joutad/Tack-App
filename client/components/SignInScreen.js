import {
  StyleSheet,
  View,
  Image,
  Text,
  useWindowDimensions,
  ScrollView,
} from "react-native";
import React, { useState } from "react";
import Logo from "../assets/images/logo.png";
import CustomInput from "./CustomInput/CustomInput";
import CustomButton from "./CustomButton/CustomButton";

const SignInScreen = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const { height } = useWindowDimensions();

  const onSignInPressed = () => {
    console.warn("Sign in");
  };

  const onSignInGoogle = () => {
    console.warn("Sign in with Google");
  };

  const onSignUpPress = () => {
    console.warn("Sign up Press");
  };

  return (
    <ScrollView showsVerticalScrollIndicator={false}>
      <View style={styles.root}>
        <Image
          source={Logo}
          style={[styles.logo, { height: height * 0.3 }]}
          resizeMode="contain"
        />
        <Text style={styles.title}>LOGIN</Text>
        <CustomInput
          placeholder="Username"
          value={username}
          setValue={setUsername}
        />
        <CustomInput
          placeholder="Password"
          value={password}
          setValue={setPassword}
          secureTextEntry={true}
        />

        <CustomButton text="Sign In" onPress={onSignInPressed} />
        <Text style={styles.text}>OR</Text>
        <CustomButton
          text="Sign In with Google"
          onPress={onSignInGoogle}
          bgColor="#1317DD"
          fgColor="white"
        />

        <CustomButton
          text="Don't have an account? Create one"
          onPress={onSignUpPress}
        />
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  root: {
    flex: 1,
    alignItems: "center",
    width: "100%",
    padding: 70,
  },
  logo: {
    width: "70%",
    maxWidth: 300,
    maxHeight: 200,
    height: 100,
    margin: 50,
  },
  text: {
    alignItems: "center",
    padding: 5,
  },
  title: {
    alignItems: "center",
    padding: 5,
    fontSize: 25,
    fontWeight: "bold",
  },
});

export default SignInScreen;
