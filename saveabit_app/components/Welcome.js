import React from 'react';
import { View, Text, Button } from 'react-native';

const WelcomePage = () => {
  return (
    <View>
      <Text>Ecoswap</Text>
      <View >
        <Text>Please select your role to get started!</Text>
        <Button title="Partner"></Button>
        <Button title="Shopper"></Button>
        <Text>Food for all</Text>
        </View>
    </View>
  );
};

export default WelcomePage;
