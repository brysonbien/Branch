import { Image, Text, View, StyleSheet, Platform, TouchableOpacity, Button,TextInput, Pressable} from 'react-native';

import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import React, { useState } from 'react';
import PhotoUpload from 'react-native-photo-upload';

export type CreateEventProps = {
  handleCreate: (...args: any[]) => void;
};


export default function CreateEvent({
  handleCreate
}: CreateEventProps) {
  const [name, setName] = useState("")
  const [location, setLocation] = useState("")



  const handleSave = () => {
    console.log("Event Created")
    handleCreate()
  }

  return (
    <ThemedView style={styles.container}>      
      <Text style={styles.inputText}>Event Name</Text>
      <TextInput
        style={styles.input}
        placeholder="Event Name"
        placeholderTextColor="#aaa"
        value={name}
        onChangeText={setName}
        autoCapitalize="none"
      />
      <Text style={styles.inputText}>Event Location</Text>
      <TextInput
        style={styles.input}
        placeholder="Location"
        placeholderTextColor="#aaa"
        value={location}
        onChangeText={setLocation}
        autoCapitalize="none"
      />
      <TouchableOpacity style={styles.button} onPress={handleSave}>
        <Text style={styles.buttonText}>Create Event</Text>
      </TouchableOpacity>

    </ThemedView>
  );
}

const styles = StyleSheet.create({
  interestButtonText: {
    color: '#fff',
    fontSize: 14,
    fontWeight: 'bold'
  }, 
  interestButton: {
    height: 40,
    width: 50,
    marginLeft: 10,
    backgroundColor: '#008000',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 8,
  },
  interestContainer: {
    flexDirection: 'row',
  },
  container: {
    flex: 1,
    padding: 32,
    gap: 16,
    overflow: 'scroll',
  },
  name: {
    marginTop: 50,
    marginBottom: 20,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  location: {
    marginTop: 20,
    marginBottom: 20,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  titleContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  profilePicContainer: {
    marginTop: 20,
    marginBottom: 20,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  profilePic: {
    width: 150,
    height: 150,
    borderRadius: 100,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
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
  inputText: {
    fontSize: 16,
    fontWeight: 'bold'
  },
  button: {
    width: '100%',
    height: 40,
    backgroundColor: '#008000',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 8,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  multiSelect: {
    backgroundColor: '#fff',
    borderRadius: 10,
    borderColor: '#ddd',
    borderWidth: 1,
    padding: 10,
  },
  searchInput: {
    backgroundColor: '#f0f0f0',
    borderColor: '#ddd',
    borderWidth: 1,
    borderRadius: 5,
    padding: 10,
  },
  listContainer: {
    maxHeight: 200, // Set max height to enable scrolling if there are many items
  },
});
