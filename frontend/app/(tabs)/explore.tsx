import Ionicons from '@expo/vector-icons/Ionicons';
import { StyleSheet, Image, Platform, ScrollView, Text,View, TouchableOpacity, Pressable} from 'react-native';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import React, { useState } from 'react';
import UserProfile from '@/components/UserProfile'

interface LineWithTextProps {
  text: string;
}

const LineWithText: React.FC<LineWithTextProps> = ({text}) => {
  return (
    <View style={styles.lineContainer}>
      <View style={styles.line} />
      <Text style={styles.lineText}>{text}</Text>
      <View style={styles.line} />
    </View>
  );
};

export default function TabTwoScreen() {
  const [interest, useInterest] = useState(false)
  const [isProfile, setIsProfile] = useState(false)
  const [username, setUsername] = useState("")

  const users = [{name: 'John', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPJtydZePQWuOVtLT7i6w_b9UpG26ZVX6JsQ&s',
    interests: ['Programming', 'Mathmatic']
  },
  {name: 'Tony', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    interests: ['Guitar', 'Gaming']
  },
  {name: 'Jenny', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCrHqWRNVBgP3y8V5VGudA0f5UmnisaLBGpA&s',
    interests: ['Music', 'Gaming', 'Moview']
  }]

  const users2 = [{name: 'john_doe', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVoa9cpYPXd8OR8J9Zz8vw4Kj421p9GTikrg&s',
    interests: ['Music', 'Gaming', 'Hiking', 'Thinking', 'Japanese']
  },
  {name: 'Tony', pic: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9mjn-XEoZoql762QQVg4agiWEFZcqs94tHg&s',
    interests: ['Guitar', 'Gaming', 'Jerking']
  },
  {name: 'Darius', pic: 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    interests: ['Music', 'Gaming', 'Squashing']
  }]

  const getUserProfile = (nameSet:string) => {
    setUsername(nameSet)
    // setIsProfile(true)
  }
  
  return (
    <>
      {!isProfile &&
        <ScrollView contentContainerStyle={styles.container}>
          <View style={styles.textContainer}>
            <Text style={styles.mainText}>Explore</Text>
          </View>
          <TouchableOpacity onPress={() => {useInterest(!interest)}} style={styles.filter}>
            <Text style={styles.filterText}>{interest ? "Without Filter" : "Filter Interests"}</Text>
          </TouchableOpacity>
          <LineWithText text="recommended"></LineWithText>
          <View style={styles.userAllContainer}>
            {users.map((user, index) => (
              <Pressable onPress={() => getUserProfile(user.name)} style={styles.userContainer}>
                <View style={styles.photoContaienr}>
                  <Image
                    source={{uri: user.pic}}
                    style={styles.picture}
                  ></Image>
                  <Text style={styles.userText}>{user.name}</Text>
                </View>
                <View style={styles.pillContainer}>
                  {user.interests.map((interest, index) => (
                    <TouchableOpacity style={styles.pill}>
                      <Text style={styles.pillText}>{interest}</Text>
                    </TouchableOpacity>
                  ))}
                </View>
              </Pressable>
            ))}
          </View>
          <LineWithText text="all"></LineWithText>
          <View style={styles.userAllContainer}>
            {users2.map((user, index) => (
              <View style={styles.userContainer}>
                <View style={styles.photoContaienr}>
                  <Image
                    source={{uri: user.pic}}
                    style={styles.picture}
                  ></Image>
                  <Text style={styles.userText}>{user.name}</Text>
                </View>
                <View style={styles.pillContainer}>
                  {user.interests.map((interest, index) => (
                    <TouchableOpacity style={styles.pill}>
                      <Text style={styles.pillText}>{interest}</Text>
                    </TouchableOpacity>
                  ))}
                </View>
              </View>
            ))}
          </View>
        </ScrollView>
      }
      {isProfile &&
        <UserProfile
          username = {username}
          back={() => {setIsProfile(false)}}
        ></UserProfile>
      }
    </>
  );
}

const styles = StyleSheet.create({
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
    marginHorizontal: 10,
    fontSize: 12, // Small text size
    color: '#808080', // Text color
  },
});
