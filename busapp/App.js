import React, { useState } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

const Header = ({ title }) => (
  <View style={styles.header}>
    <Text>{title}</Text>
  </View>
);

const HomeScreen = ({ navigateTo }) => (
  <View style={styles.container}>
    <Text>Home Screen</Text>
    <Button title="Go to Link1" onPress={() => navigateTo('Link1')} />
    <Button title="Go to Link2" onPress={() => navigateTo('Link2')} />
  </View>
);

const Link1Screen = ({ navigateTo }) => (
  <View style={styles.container}>
    <Text>Link1 Screen</Text>
    <Button title="Go back" onPress={() => navigateTo('Home')} />
  </View>
);

const Link2Screen = ({ navigateTo }) => (
  <View style={styles.container}>
    <Text>Link2 Screen</Text>
    <Button title="Go back" onPress={() => navigateTo('Home')} />
  </View>
);

export default function App() {
  const [screen, setScreen] = useState('Home');

  const navigateTo = (screenName) => {
    setScreen(screenName);
  };

  return (
    <View style={styles.container}>
      <Header title={screen} />
      {screen === 'Home' && <HomeScreen navigateTo={navigateTo} />}
      {screen === 'Link1' && <Link1Screen navigateTo={navigateTo} />}
      {screen === 'Link2' && <Link2Screen navigateTo={navigateTo} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  header: {
    height: 50,
    width: '100%',
    backgroundColor: '#f8f8f8',
    justifyContent: 'center',
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
  },
});