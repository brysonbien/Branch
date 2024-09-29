import { Image,TouchableOpacity, StyleSheet, Platform , ScrollView, View, Text} from 'react-native';
import {base_url} from '@/constants/apiRoute'

import EvenView from '@/components/EventView';
import React, { useState, useEffect } from 'react';
import CreateEvent from '../createEvent';
// import { MMKV, useMMKVString} from 'react-native-mmkv'

export default function HomeScreen() {
  const events = [{eventname: "Taloy Swift Concert", eventdate: "2024-07-24", profileInfo: [{name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}, 
    {name: 'Micheal', pic: 'https://wallpapers.com/images/hd/profile-picture-f67r1m9y562wdtin.jpg'}
  ]},
  {eventname: "Football game", eventdate: "2024-08-12", profileInfo: [{name: 'Mia', pic: 'https://play-lh.googleusercontent.com/jInS55DYPnTZq8GpylyLmK2L2cDmUoahVacfN_Js_TsOkBEoizKmAl5-p8iFeLiNjtE=w526-h296-rw'}, 
    {name: 'Erica', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjgozuCfOm6KK6d5WM06498mrXzZB12TawhA&s'},
    {name: 'Anna', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4q4WLuAzSHosjkVws4BwFSEEHbg3npY5rWA&s'}
  ]},
  {eventname: "Micheal Jackson Concert", eventdate: "2024-08-20", profileInfo: [{name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}
  ]}
  ]

  const [create, setCreate] = useState(false)
  // const [username, setUsername] = useMMKVString('user.name')
  // const [events, setEvents] = useState([])

  // const getUserInfo = async () => {
  //   try {
  //     const userData = {
  //       username: username,
  //     }
  //     const response = await fetch(base_url + '/init', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //         'Access-Control-Allow-Origin': base_url
  //       },
  //       body: JSON.stringify(userData),
  //     });
  
  //     if (!response.ok) {
  //       return false;
  //     }
  //     const data = await response.json();
  //     console.log('Data from Flask:', data);
  //     return await getEventPages()
  //   } catch (error) {
  //     console.error('There was a problem with the fetch operation:', error);
  //   }  
  // }

  const getEventPages = async () => {
    try {
      const response = await fetch(base_url + '/myeventspage', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': base_url
        },
      });

      if (!response.ok) {
        return false;
      }
      console.log(response)
      const data = await response.json();
      var singleEvent = {eventName: data.EventName, eventDate: data.EventDate, eventLocation: data.EventLocation}
      console.log('Data from Flask:', data);
      return true;
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  }

  useEffect(() => {
    // getUserInfo()
    getEventPages()
    // console.log(username)
  },[create]);

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
