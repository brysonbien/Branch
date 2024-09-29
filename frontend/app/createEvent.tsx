import { Image, Text, View, StyleSheet, Platform, TouchableOpacity, Button,TextInput, Pressable} from 'react-native';

import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import React, { useState } from 'react';
import PhotoUpload from 'react-native-photo-upload';
import AntDesign from '@expo/vector-icons/AntDesign';
import {base_url} from '@/constants/apiRoute'

export type CreateEventProps = {
  handleCreate: (...args: any[]) => void;
  setEventName: (...args: any[]) => void;
  setDate: (...args: any[]) => void;
};


export default function CreateEvent({
  handleCreate,
  setEventName,
  setDate
}: CreateEventProps) {
  const [name, setName] = useState("")
  const [location, setLocation] = useState("")
  const [time, setTime] = useState("")
  const [description, setDescription] = useState("")
  const [username, setUsername] = useState("")

  // const getUsername = async () => {
  //   try {
  //     const response = await fetch(base_url + '/getusername', {
  //       method: 'GET',
  //       headers: {
  //         'Content-Type': 'application/json',
  //         'Access-Control-Allow-Origin': base_url
  //       },
  //     });

  //     if (!response.ok) {
  //       return false;
  //     }
  //     const data = await response.text();
  //     setUsername(data)
  //     console.log('Data from Flask:', data);
  //     return true;
  //   } catch (error) {
  //     console.error('There was a problem with the fetch operation:', error);
  //   }
  // }

  // const createEvent = async () => {
  //   try {
  //     const eventData = {
  //       username: "rebelxhawk",
  //       EventName: name,
  //       Location: location,
  //       EventDate: "2024-" + time + " 10:45:00",
  //       EventDescripton: description
  //     }
  //     console.log(eventData)
  //     const response = await fetch(base_url + '/createevent', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //         'Access-Control-Allow-Origin': base_url
  //       },
  //       body: JSON.stringify(eventData),
  //     });
  
  //     if (!response.ok) {
  //       return false;
  //     }
  
  //     const data = await response.json();
  //     console.log('Data from Flask:', data);
  //     return true;
  //   } catch (error) {
  //     console.error('There was a problem with the fetch operation:', error);
  //   }
  // }

  const handleSave = async () => {
    // if (await getUsername()) {
      // if (await createEvent()) {
      setEventName(name)
      setDate(time)
      handleCreate()
      // }
    // }
  }

  return (
    <ThemedView style={styles.container}>      
      <TouchableOpacity style={styles.backButton} onPress={handleCreate}>
        <AntDesign name="back" size={20} color="white" />
      </TouchableOpacity>
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
      <Text style={styles.inputText}>Date Time</Text>
      <TextInput
        style={styles.input}
        placeholder="Date Time"
        placeholderTextColor="#aaa"
        value={time}
        onChangeText={setTime}
        autoCapitalize="none"
      />
      <Text style={styles.inputText}>Description</Text>
      <TextInput
        style={styles.inputBox}
        multiline={true}
        // numberOfLines={4}    
        placeholder="Description"
        placeholderTextColor="#aaa"
        value={description}
        onChangeText={setDescription}
        autoCapitalize="none"
      />
      <TouchableOpacity style={styles.button} onPress={handleSave}>
        <Text style={styles.buttonText}>Create Event</Text>
      </TouchableOpacity>

    </ThemedView>
  );
}

const styles = StyleSheet.create({
  backButton: {
    width: 50,
    height: 35,
    backgroundColor: '#008000',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 8,
  },
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
  inputBox: {
    width: '100%',
    height: 100,
    backgroundColor: '#fff',
    borderRadius: 8,
    paddingHorizontal: 15,
    paddingTop: 10,
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
