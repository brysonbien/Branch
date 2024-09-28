import { Image,TouchableOpacity, StyleSheet, Platform , ScrollView, View, Text} from 'react-native';

import EvenView from '@/components/EventView';
import React, { useState, useEffect } from 'react';
import CreateEvent from '../createEvent';
import { MMKV, useMMKVString} from 'react-native-mmkv'

export default function HomeScreen() {
  const events = [{eventname: "Taloy Swift Concert", eventdate: "2024-07-24", profileInfo: [{name: 'Thomas', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}, 
    {name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}
  ]},
  {eventname: "Football game", eventdate: "2024-07-24", profileInfo: [{name: 'Thomas', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}, 
    {name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}
  ]},
  {eventname: "Micheal Jackson Concert", eventdate: "2024-07-24", profileInfo: [{name: 'Thomas', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}, 
    {name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}
  ]}
]

const [create, setCreate] = useState(false)
const [username, setUsername] = useMMKVString('user.name')

  useEffect(() => {
    console.log(username)
  },[]);

  return (
    <>
    {!create &&
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.button} onPress={() => {setCreate(true)}}>
            <Text style={styles.buttonText}>Create</Text>
          </TouchableOpacity>
        </View>
        {events.map((customEvent, index) => (
          <View style={styles.eventContainer}>
            <EvenView
              EventName={customEvent.eventname}
              EventDate={customEvent.eventdate}
              ProfileInfo={customEvent.profileInfo}
            ></EvenView>
          </View>
        ))}
      </ScrollView>
    }
    {create &&
      <CreateEvent
        handleCreate={() => {setCreate(false)}}
      />
    }
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    paddingTop: 20,
    justifyContent: 'flex-start',
    backgroundColor: 'white',
    paddingBottom: "100%"
    // height: "100%"
  },
  eventContainer: {
    marginTop: 10
  },
  buttonContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  button: {
    width: '80%', // Or you can use a fixed width like 300
    height: 40,
    backgroundColor: '#008000',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 8,
  },
  buttonText: {
    color: '#FFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
