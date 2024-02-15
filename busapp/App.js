import React, { useState } from 'react';
import { StyleSheet, Text, View, Image, TextInput, Button, Alert } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';

const Drawer = createDrawerNavigator();

function RegisterScreen() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const register = () => {
    fetch('http://127.0.0.1:8000/bus/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `username=${username}&password=${password}`,
    })
    .then(response => {
      if (!response.ok) {
        return response.text().then(text => {
          console.log('Response text:', text);  // log the response text
          throw new Error(text);
        });
      }
      return response.json();
    })
    .then(data => {
      if (data.error) {
        Alert.alert('Error', data.error);
      } else {
        Alert.alert('Success', data.message);
      }
    })
    .catch(error => Alert.alert('Error', error.toString()));
  };

  return (
    <View>
      <TextInput placeholder="Username" onChangeText={setUsername} />
      <TextInput placeholder="Password" onChangeText={setPassword} secureTextEntry />
      <Button title="Register" onPress={register} />
    </View>
  );
}

function LoginScreen() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const login = () => {
    fetch('http://127.0.0.1:8000/bus/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `username=${username}&password=${password}`,
    })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        Alert.alert('Error', data.error);
      } else {
        Alert.alert('Success', data.message);
      }
    });
  };

  return (
    <View>
      <TextInput placeholder="Username" onChangeText={setUsername} />
      <TextInput placeholder="Password" onChangeText={setPassword} secureTextEntry />
      <Button title="Login" onPress={login} />
    </View>
  );
}

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
        <Drawer.Screen name="Register" component={RegisterScreen} />
        <Drawer.Screen name="Login" component={LoginScreen} />
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