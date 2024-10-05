import React from 'react';
import { Text, View, TextInput, Button, StyleSheet } from 'react-native';

export default function SignUp() {
  const handleSignUp = () => {
    // Handle sign up logic here (e.g., validation, API call)
    alert('Sign Up button pressed');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sign Up</Text>
      <Text>Sign up to find personalized items for purchase</Text>

      <TextInput style={styles.input} placeholder="First Name" />
      <TextInput style={styles.input} placeholder="Last Name" />
      <TextInput style={styles.input} placeholder="Email" />
      <TextInput style={styles.input} placeholder="Phone Number" />
      <TextInput style={styles.input} placeholder="Password" secureTextEntry />
      <TextInput style={styles.input} placeholder="Age" keyboardType="numeric" />
      <TextInput style={styles.input} placeholder="Address" />
      <TextInput style={styles.input} placeholder="Dietary Restrictions" />
      <TextInput style={styles.input} placeholder="Allergies" />

      <Button title="Confirm" onPress={handleSignUp} />

      <Text>Already have an account? Log In</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
    backgroundColor: 'white',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    width: '100%',
    paddingHorizontal: 10,
  },
});
