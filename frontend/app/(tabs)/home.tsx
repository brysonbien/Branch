import { Image,TouchableOpacity, StyleSheet, Platform , ScrollView, View, Text} from 'react-native';
import {base_url} from '@/constants/apiRoute'

import EvenView from '@/components/EventView';
import React, { useState, useEffect } from 'react';
import CreateEvent from '../createEvent';
// import { MMKV, useMMKVString} from 'react-native-mmkv'

export default function HomeScreen() {
  const [isAdded, setIsAdded] = useState(false)
  const [create, setCreate] = useState(false)
  const [name, setName] = useState("")
  const [eventName, setEventName] = useState("")
  const [eventDate, setEventDate] = useState("")
  const [events, setEvents] = useState(Array)

  const eventInfo = [{eventname: "Taloy Swift Concert", eventdate: "2024-07-24", profileInfo: [{name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}, 
    {name: 'Micheal', pic: 'https://wallpapers.com/images/hd/profile-picture-f67r1m9y562wdtin.jpg'}
  ]},
  {eventname: "Football game", eventdate: "2024-08-12", profileInfo: [{name: 'Mia', pic: 'https://play-lh.googleusercontent.com/jInS55DYPnTZq8GpylyLmK2L2cDmUoahVacfN_Js_TsOkBEoizKmAl5-p8iFeLiNjtE=w526-h296-rw'}, 
    {name: 'Erica', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjgozuCfOm6KK6d5WM06498mrXzZB12TawhA&s'},
    {name: 'Anna', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4q4WLuAzSHosjkVws4BwFSEEHbg3npY5rWA&s'}
  ]},
  {eventname: "Micheal Jackson Concert", eventdate: "2024-08-20", profileInfo: [{name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}
  ]},
  {eventname: "Georgia Tech Data Hackathon", eventdate: "2024-09-13", profileInfo: [{name: 'Winnie', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9oyv7eDWqICKUYv8yvjZTs2x5tQRhUBvQ_A&s'},
    {name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'},
    {name: 'Mikatsu', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs9TAh2ZVlP3acVa9V3seEbOZKp7fxcbTULQ&s'},
    {name: 'Inkyung', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqOH9ife85JK3m5lBwE8YBVE40MsF5KLnCkQ&s'},
    {name: 'Jack', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZAPq07xr155Bi5zkTjI5GMjB6AB3qlk9DOw&s'},
  ]},
  {eventname: "Japanese Culture Exhibition", eventdate: "2024-09-15", profileInfo: [{name: 'Gipson', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbD-_Kg0JWpPcSer-gunVoK5r6GrzdJZRTnA&s'}, 
    {name: 'Perry', pic: 'https://www.shiguang.pro/skycaiji/data/images/5c/b9c9a29e91c2777777210a51dfe550.jpg'},
    {name: 'James', pic: 'https://p9-pc-sign.douyinpic.com/tos-cn-i-0813/163cfff64f5a4968ae2faaa7ceefe990~tplv-dy-aweme-images:q75.webp?biz_tag=aweme_images&from=327834062&s=PackSourceEnum_SEARCH&sc=image&se=false&x-expires=1730124000&x-signature=i%2BBzxjwkLQc2AD1pKiMlW1ptFoQ%3D'}
  ]},
  ]

  useEffect(() => {
    setEvents(eventInfo)
  },[])

  useEffect(() => {
    console.log(eventName.length)
    if (!isAdded && eventName.length > 0) {
      console.log("work")
      setIsAdded(true)
      events.unshift({eventname: eventName, eventdate: eventDate, profileInfo: [{name: name, pic: piclink}]})
      setEvents(events)
      console.log(events)
    }
  }, [eventName])

  // const getUserInfo = async () => {
  //   try {
  //     const response = await fetch(base_url + '/myprofilepage', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //         'Access-Control-Allow-Origin': base_url
  //       },
  //     });
  
  //     if (!response.ok) {
  //       return false;
  //     }
  //     const data = await response.json();
  //     setName(data.Name as string)
  //     console.log('Data from Flask:', data);
  //     return true;
  //   } catch (error) {
  //     console.error('There was a problem with the fetch operation:', error);
  //   }
  // }  

  const piclink = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
  // const [username, setUsername] = useMMKVString('user.name')
  // const [events, setEvents] = useState([])

  // const getEventPages = async () => {
  //   try {
  //     const response = await fetch(base_url + '/myeventspage', {
  //       method: 'GET',
  //       headers: {
  //         'Content-Type': 'application/json',
  //         'Access-Control-Allow-Origin': base_url
  //       },
  //     });

  //     if (!response.ok) {
  //       return false;
  //     }
  //     console.log(response)
  //     const data = await response.json();
  //     var singleEvent = {eventName: data.EventName, eventDate: data.EventDate, eventLocation: data.EventLocation}
  //     console.log('Data from Flask:', data);
  //     return true;
  //   } catch (error) {
  //     console.error('There was a problem with the fetch operation:', error);
  //   }
  // }

  // useEffect(() => {
  //   // getUserInfo()
  //   // getEventPages()
  //   // console.log(username)
  // },[create]);

  return (
    <>
    {!create &&
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.button} onPress={() => {setIsAdded(false); setCreate(true)}}>
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
        setEventName={setEventName}
        setDate={setEventDate}
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
    paddingBottom: "40%"
    // height: "100%"
  },
  eventContainer: {
    // justifyContent: 'flex-start',
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
