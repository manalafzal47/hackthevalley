import { Text, View, Button, StyleSheet } from 'react-native';
import Welcome from '../../components/Welcome';
import SignUp from '../../components/SignUp';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Welcome />
      <SignUp/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1, 
    justifyContent: 'center',
    alignItems: 'center', 
    backgroundColor: 'white', 
  },
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
