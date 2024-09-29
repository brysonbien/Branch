import { StyleSheet, Image, Platform, ScrollView, Text,View, TouchableOpacity, Pressable} from 'react-native';

import ParallaxScrollView from '@/components/ParallaxScrollView';
import React, { useState } from 'react';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';

export default function Chat() {
  const [inChat, setInChat] = useState(false)

  const users = [{name: 'john_doe', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    interests: ['Music', 'Gaming', 'Hiking', 'Thinking', 'Japanese']
  },
  {name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    interests: ['Guitar', 'Gaming', 'Jerking']
  },
  {name: 'Darius', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    interests: ['Music', 'Gaming', 'Squashing']
  }]

  const goToChat = (receiver:string) => {

  }

  return (
    <>
      {!inChat &&
        <ScrollView contentContainerStyle={styles.container}>
          <View style={styles.textContainer}>
            <Text style={styles.mainText}>Chat</Text>
          </View>
          <View style={styles.userAllContainer}>
            {users.map((user, index) => (
              <View style={styles.chatContainer}>
                <View style={styles.lineContainer}>
                  <View style={styles.line} />
                </View>
                <Pressable onPress={() => goToChat(user.name)} style={styles.userContainer}>
                  <View style={styles.photoContaienr}>
                    <Image
                      source={{uri: user.pic}}
                      style={styles.picture}
                    ></Image>
                    <Text style={styles.userText}>{user.name}</Text>
                  </View>
                </Pressable>
              </View>
            ))}
          </View>
        </ScrollView>
      }
      {inChat &&
      <></>
      }
    </>

  );
}

const styles = StyleSheet.create({
  chatContainer: {
    width: "100%"
  },
  filter: {
    marginTop: 10,
    backgroundColor: '#008000', // Pill background color
    borderRadius: 20,          // Make it pill-shaped
    paddingVertical: 5,       // Vertical padding
    paddingHorizontal: 5,     // Horizontal padding
    margin: 5,                 // Space between pills
    alignItems: 'center',
    justifyContent: 'center',
    width: "80%",
    height: 30
  },
  filterText: {
    color: 'white',            // Text color
    // fontWeight: 'bold',        // Bold text
    fontSize: 15
  },
  photoContaienr: {
    flexDirection: 'row',
    justifyContent: "flex-start",
    alignItems:'center'
  },
  pillContainer: {
    paddingLeft: "5%",
    flexDirection: 'row',
    flexWrap: 'wrap', // Allows the items to wrap onto the next line
    justifyContent: 'flex-start', // Align items to the start
    width: "50%",
    marginRight: 20
  },
  userText: {
    marginLeft: 10,
    fontSize: 20,
  },
  picture: {
    width: 40,
    height: 40,
    borderRadius: 100, 
    marginLeft: 10,
  },
  userContainer: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    marginTop: 20,
    height: "30%"
  },
  userAllContainer: {
    marginLeft: 20,
    paddingBottom: 40
  },
  textContainer: {
    alignItems: 'center'
  },
  mainText: {
    fontSize: 20,
    alignItems: 'center',
    fontWeight: 'bold'
  },
  container: {
    justifyContent: 'flex-start',
    alignItems: 'center',
    backgroundColor: 'white',
    paddingTop: 20,
    paddingBottom: "50%"
  },
  pill: {
    backgroundColor: '#008000', // Pill background color
    borderRadius: 20,          // Make it pill-shaped
    paddingVertical: 5,       // Vertical padding
    paddingHorizontal: 5,     // Horizontal padding
    margin: 5,                 // Space between pills
    alignItems: 'center'
  },
  pillText: {
    color: 'white',            // Text color
    fontWeight: 'bold',        // Bold text
    fontSize: 10
  },
  lineContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '100%',
    marginTop: 20,
  },
  line: {
    flex: 1,
    height: 1,
    backgroundColor: '#808080', // Color of the line
  },
  lineText: {
    // marginHorizontal: 10,
    fontSize: 12, // Small text size
    color: '#808080', // Text color
  },
});
