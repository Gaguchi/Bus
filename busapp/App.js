import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';

const Drawer = createDrawerNavigator();

function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text>This is the header</Text>
      </View>
      <Text>Hello there Betochka!!!</Text>
      <Text>Let me show this website here!</Text>
      <View style={styles.footer}>
        <Text>This is the footer</Text>
      </View>
    </View>
  );
}

function Link1Screen() {
  return (
    <View style={styles.container}>
      <Text>Link 1</Text>
    </View>
  );
}

function Link2Screen() {
  return (
    <View style={styles.container}>
      <Text>Link 2</Text>
    </View>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Home" component={HomeScreen} />
        <Drawer.Screen name="Link1" component={Link1Screen} />
        <Drawer.Screen name="Link2" component={Link2Screen} />
      </Drawer.Navigator>
    </NavigationContainer>
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
    position: 'absolute',
    top: 0,
    height: 50,
    width: '100%',
    backgroundColor: '#f8f8f8',
    alignItems: 'center',
    justifyContent: 'center',
  },
  footer: {
    position: 'absolute',
    bottom: 0,
    height: 50,
    width: '100%',
    backgroundColor: '#f8f8f8',
    alignItems: 'center',
    justifyContent: 'center',
  },
});