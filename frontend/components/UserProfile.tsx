import { Image, Text, View, StyleSheet, Platform, TouchableOpacity, Button} from 'react-native';

import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import EventView from '@/components/EventView';
import React, { useEffect, useState } from 'react';
import {base_url} from '@/constants/apiRoute'
import AntDesign from '@expo/vector-icons/AntDesign';

export type UserProfileProp = {
  username: string;
  back: (...args: any[]) => void;
};

export default function UserProfile({
  username,
  back
}: UserProfileProp) {
  const [name, setName] = useState("loading...")
  const [location, setLocation] = useState("loading...")
  const [interests, setInterests] = useState(Array<string>)

  useEffect(() => {
    getUserInfo()
  }, [])

  const getUserInfo = async () => {
    try {
      const userData = {
        username: username,
      }
      const response = await fetch(base_url + '/myprofilepage', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': base_url
        },
        body: JSON.stringify(userData),
      });
  
      if (!response.ok) {
        return false;
      }
      const data = await response.json();
      setName(data.Location as string)
      setLocation(data.Location as string)
      setInterests(data.InterestList as Array<string>)
      console.log('Data from Flask:', data);
      return true;
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  }  
  const eventname = "Taloy Swift Concert"
  const eventdate = "2024-07-24"
  const profileInfo = [{name: 'Thomas', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}, 
    {name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}
  ]

  return (
    <>
      {
        <ThemedView style={styles.container}>
          <TouchableOpacity style={styles.backButton} onPress={back}>
            <AntDesign name="back" size={20} color="white" />
          </TouchableOpacity>
          <ThemedView style={styles.name}>
            <ThemedText type="title2">{name}</ThemedText>
          </ThemedView>
          <ThemedView style={styles.profilePicContainer}>
            <Image
              source={require('@/assets/images/profile_demo.png')}
              style={styles.profilePic}
            />
          </ThemedView>
          <ThemedView style={styles.location}>
            <ThemedText type="title2">{location}</ThemedText>
          </ThemedView>
          <ThemedView style={styles.interest}>
            {interests.map((interest, index) => (
              <TouchableOpacity key={index} style={styles.pill}>
                <Text style={styles.pillText}>{interest}</Text>
              </TouchableOpacity>
            ))}
          </ThemedView>
          <ThemedView style={styles.location}>
            <EventView EventName={eventname} EventDate={eventdate} ProfileInfo={profileInfo}></EventView>
          </ThemedView>
        </ThemedView> 
      }
    </>
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
    marginTop: 32,
    marginLeft: 32
  },
  container: {
    flex: 1,
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
    justifyContent: 'center',
    flexDirection: 'row',
    flexWrap: 'wrap', // Allows pills to wrap to the next line
    margin: 20,
  },
  interestText: {
    alignContent: 'center'
  },
  pill: {
    backgroundColor: '#008000', // Pill background color
    borderRadius: 20,          // Make it pill-shaped
    paddingVertical: 10,       // Vertical padding
    paddingHorizontal: 15,     // Horizontal padding
    margin: 5,                 // Space between pills
  },
  pillText: {
    color: 'white',            // Text color
    fontWeight: 'bold',        // Bold text
  },
  button: {
    marginLeft: 20,
  }
});
