import { Image, View, Text, StyleSheet, Pressable, TouchableOpacity, Alert } from 'react-native';
import { useThemeColor } from '@/hooks/useThemeColor';
import React, { useState } from 'react';
import openMap from 'react-native-open-maps';

interface Profile {
  name: string;
  pic: string;
}

export type EventViewProp = {
  EventName: string;
  EventDate: string;
  ProfileInfo: Array<Profile>;
};

export default function EventView({
  EventName,
  EventDate,
  ProfileInfo,
}: EventViewProp) {
  const [expand, setExpand] = useState(false)

  const toggleExpand = () => {
    setExpand(!expand)
  }

  const addEvent = () => {
    console.log("event added")  
  }

  const toMap = () => {
    openMap({ 
      latitude: 37.78825, 
      longitude: -122.4324,
      zoom: 16,
      query: EventName
    });  
  }

  return (
    <Pressable onPress={toggleExpand} style={styles.container}>
      <View style={[styles.roundContainer, , expand ? styles.expand : styles.collapse]}>
        <View style={styles.textContainer}>
          <Text style={styles.eventName}>{EventName}</Text>
          <Text style={styles.eventDate}>{EventDate}</Text>
        </View>
        {!expand && (
          <View style={styles.pictureContainer}>
            {ProfileInfo.map((content, index) => (
              <Image
                source={{uri: content.pic}}
                style={styles.picture}
                key={index}
              ></Image>
            ))}
            <TouchableOpacity onPress={addEvent} style={styles.button}>
              <Text style={styles.buttonText}>+</Text>
            </TouchableOpacity>
          </View>
        )}
        {expand && (
          <View style={styles.pictureContainerExpand}>
            {ProfileInfo.map((content, index) => (
              <View style={styles.picText} key={index}>
                <Image
                  source={{uri: content.pic}}
                  style={styles.picture}
                ></Image>
                <Text style={styles.username}>{content.name} {index == 0 && "(Creator)"}</Text>
              </View>
            ))}
            <TouchableOpacity onPress={toMap}>
              <Image style={styles.picture}
              source={require("@/assets/images/googlemaps.png")}></Image>
            </TouchableOpacity>
            <TouchableOpacity onPress={addEvent} style={styles.button}>
              <Text style={styles.buttonText}>+</Text>
            </TouchableOpacity>
          </View>
        )}
      </View>
    </Pressable>
  );
}

const styles = StyleSheet.create({
    username: {
      marginLeft: 10,
      marginTop: 20,
      color: 'white',            // Text color
      fontSize: 14,
    },
    picText: {
      flexDirection: 'row',
      justifyContent: 'flex-start'
    },
    pictureContainer: {
      marginTop: 20,
      marginLeft: 10,
      alignItems: 'flex-start',
      flexDirection: 'row',
    },
    pictureContainerExpand: {
      marginTop: 20,
      marginLeft: 10,
      alignItems: 'flex-start',
    }, 
    picture: {
      width: 40,
      height: 40,
      borderRadius: 100, 
      marginLeft: 10,
      marginTop: 10
    },
    container: {
      flex: 1,
      justifyContent: 'center', // Center the round container
      alignItems: 'center',
    },
    roundContainer: {
      width: 350,               // Set the width of the round container
      borderRadius: 25,         // Make it circular
      backgroundColor: '#008000', // Background color
      justifyContent: 'flex-start',  // Center text vertically
      elevation: 4,              // Shadow for Android
      shadowColor: '#000',       // Shadow color for iOS
      shadowOffset: { width: 0, height: 2 }, // Shadow offset
      shadowOpacity: 0.2,        // Shadow opacity
      shadowRadius: 4,           // Shadow radius
    },
    collapse: {
      height: 150
    }, 
    expand: {
      paddingBottom: 20
    },
    eventName: {
      marginTop: 10,
      color: 'white',            // Text color
      fontWeight: 'bold',        // Bold text
      fontSize: 16,              // Font size
      // textAlign: 'center',       // Center the text
    },
    eventDate: {
      marginTop: 10,
      color: 'white',            // Text color
      fontSize: 14,              // Font size
      // textAlign: 'center',       // Center the text
    },
    textContainer: {
      alignItems: 'center',      // Center text horizontally
    },
    button: {
      marginLeft: 10,
      marginTop: 10,
      width: 40,  // Width of the button
      height: 40, // Height of the button
      borderRadius: 100, // Half of the width/height to make it rounded
      backgroundColor: '#007BFF', // Button color
      justifyContent: 'center', // Center the content vertically
      alignItems: 'center', // Center the content horizontally
    },
    buttonText: {
      marginBottom: 5,
      fontSize: 30, // Size of the plus sign
      color: '#FFFFFF', // Text color
    },
});
