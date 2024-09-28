import { Image, Text, View, StyleSheet, Platform, TouchableOpacity, Button,TextInput, Pressable} from 'react-native';

import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import React, { useState } from 'react';

export type UserEditProps = {
  Username: string;
  Location: string;
  Interest: Array<string>;
  handleEdit: (...args: any[]) => void;
};


export default function UserEdit({
  Username,
  Location,
  Interest,
  handleEdit
}: UserEditProps) {
  const [username, setUsername] = useState(Username)
  const [location, setLocation] = useState(Location)
  const [interests, setInterests] = useState(Interest);
  const [interest, setInterest] = useState("")

  const addInterest = () => {
    if (interests.indexOf(interest) == -1) {
      setInterests(interests => [...interests, interest])
    }
    setInterest("")
  };

  const removeInterest = (index: any) => {
    setInterests(interests => {
      const newInterests = interests.filter((_, i) => i !== index); // Create new array without the item at index
      return newInterests;
    });
  }

  const handleSave = () => {
    console.log("save")
    handleEdit()
  }

  return (
    <ThemedView style={styles.container}>
      <ThemedView style={styles.profilePicContainer}>
        <Image
          source={require('@/assets/images/profile_demo.png')}
          style={styles.profilePic}
        />
      </ThemedView>
      
      <Text style={styles.inputText}>Username</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        placeholderTextColor="#aaa"
        value={username}
        onChangeText={setUsername}
        autoCapitalize="none"
      />
      <Text style={styles.inputText}>Location</Text>
      <TextInput
        style={styles.input}
        placeholder="Location"
        placeholderTextColor="#aaa"
        value={location}
        onChangeText={setLocation}
        autoCapitalize="none"
      />
      <Text style={styles.inputText}>Interests</Text>
      <View style={styles.interestContainer}>
        <TextInput
          style={styles.input}
          placeholder="Interest"
          placeholderTextColor="#aaa"
          value={interest}
          onChangeText={setInterest}
          autoCapitalize="none"        
        />
        <Pressable onPress={addInterest} style={styles.interestButton}>
            <Text style={styles.interestButtonText}>
              add
            </Text>
          </Pressable>
      </View>
      <ThemedView style={styles.interest}>
        {interests.map((interest, index) => (
          <TouchableOpacity key={index} style={styles.pill} onPress={() => removeInterest(index)}>
            <Text style={styles.pillText}>{interest}</Text>
          </TouchableOpacity>
        ))}
      </ThemedView>
      <TouchableOpacity style={styles.button} onPress={handleSave}>
        <Text style={styles.buttonText}>Save</Text>
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
  interest: {
    flexDirection: 'row',
    flexWrap: 'wrap', // Allows pills to wrap to the next line
  },
  interestText: {
    alignContent: 'center'
  },
  pill: {
    backgroundColor: '#008000', // Pill background color
    borderRadius: 20,          // Make it pill-shaped
    paddingVertical: 5,       // Vertical padding
    paddingHorizontal: 10,     // Horizontal padding
    margin: 5,                 // Space between pills
  },
  pillText: {
    color: 'white',            // Text color
    fontWeight: 'bold',        // Bold text
    fontSize: 12
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
