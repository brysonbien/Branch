import { Image, StyleSheet, Platform, View,Pressable,TextInput, Text } from 'react-native';

import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import React, { useState } from 'react';
import {base_url} from '@/constants/apiRoute'
import { MMKV } from 'react-native-mmkv'
import {storage} from '@/constants/mmkv'


export default function HomeScreen() {
  const [login, setLogin] = useState(false)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const jumpLogin = () => {
    setLogin(true)
  }

  const handleLogin = async () => {
    if (await instaLogin()) {
      storage.set('user.name', username)
      window.location.href = '/home'
    }
  }

  const instaLogin = async () => {
    try {
      const loginData = {
        username: username,
        password: password,
      }
      const response = await fetch(base_url + '/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': base_url
        },
        body: JSON.stringify(loginData),
      });
  
      if (!response.ok) {
        return false;
      }
  
      const data = await response.json();
      console.log('Data from Flask:', data);
      return true;
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }  
  }

  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#A1CEDC', dark: '#1D3D47' }}
      headerImage={
        <Image
          source={require('@/assets/images/branch_logo.png')}
          style={styles.reactLogo}
        />
      }>
      {!login &&
        <View style={styles.container}>
          <ThemedView style={styles.titleContainer}>
            <ThemedText type="title">Branch</ThemedText>
          </ThemedView>
          <ThemedView style={styles.titleContainer}>
            <ThemedText type="subtitle">Use Instagram to Login</ThemedText>
          </ThemedView>
          <Pressable onPress={jumpLogin} style={styles.titleContainer}>
            <Image
              source={require('@/assets/images/Instagram_icon.png')}
              style={styles.instaLogo}
            />
          </Pressable>
        </View>
      }
      {login &&
        <View style={styles.container}>
          <Text style={styles.title}>Login with Instagram</Text>
          <TextInput
            style={styles.input}
            placeholder="Username"
            placeholderTextColor="#aaa"
            value={username}
            onChangeText={setUsername}
            autoCapitalize="none"
          />
          <TextInput
            style={styles.input}
            placeholder="Password"
            placeholderTextColor="#aaa"
            value={password}
            onChangeText={setPassword}
            secureTextEntry={true}
          />
          <Pressable style={styles.button} onPress={handleLogin}>
            <Text style={styles.buttonText}>Login</Text>
          </Pressable>
        </View>
      }
      
    </ParallaxScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  titleContainer: {
    flexDirection: 'row',
    gap: 8,
    padding: 10
  },
  instaLogo: {
    width: 150,
    height: 150,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    top: 0,
    height: "100%",
    width: "100%",
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#333',
  },
  input: {
    width: '100%',
    height: 40,
    backgroundColor: '#fff',
    borderRadius: 8,
    paddingHorizontal: 15,
    marginBottom: 15,
    borderColor: '#ddd',
    borderWidth: 1,
    fontSize: 16,
  },
  button: {
    width: '100%',
    height: 40,
    backgroundColor: '#008000',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 8,
    marginTop: 20,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
