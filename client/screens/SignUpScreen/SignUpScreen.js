import { StyleSheet, View, Text, ScrollView } from "react-native";
import React, { useState } from "react";
import CustomInput from "../../components/CustomInput/CustomInput";
import CustomButton from "../../components/CustomButton/CustomButton";

const SignUpScreen = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordRepeat, setPasswordRepeat] = useState("");

  const onRegisterPressed = () => {
    console.warn("on Register Pressed");
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
        <Text style={styles.title}>Create an account</Text>
        <CustomInput
          placeholder="Username"
          value={username}
          setValue={setUsername}
        />
        <CustomInput placeholder="Email" value={email} setValue={setEmail} />
        <CustomInput
          placeholder="Password"
          value={password}
          setValue={setPassword}
          secureTextEntry
        />
        <CustomInput
          placeholder="Repeat Password"
          value={passwordRepeat}
          setValue={setPasswordRepeat}
          secureTextEntry
        />

        <CustomButton text="Register" onPress={onRegisterPressed} />
        <Text style={styles.text}>
          By registering, you confirm that you accept our{" "}
          <Text style={styles.link}>Terms of Use</Text> and{" "}
          <Text style={styles.link}>Privacy Policy</Text>
        </Text>
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
    color: "gray",
    marginVertical: 10,
  },
  link: {
    color: "#FDB075",
  },
  title: {
    alignItems: "center",
    padding: 5,
    fontSize: 24,
    fontWeight: "bold",
    color: "#051C60",
    margin: 10,
  },
});

export default SignUpScreen;
