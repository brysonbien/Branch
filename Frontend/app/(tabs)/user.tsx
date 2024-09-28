import { Image, Text, View, StyleSheet, Platform, TouchableOpacity, Button} from 'react-native';

import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import EventView from '@/components/EventView';


export default function HomeScreen() {

  const name = "Thomas"
  const location = "Atlanta"
  const interests = ['Music', 'Travel', 'Reading', 'Cooking', 'Gaming']
  const isUser = true
  const eventname = "Taloy Swift Concert"
  const eventdate = "2024-07-24"
  const profilePic = ['https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 'https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2']

  return (
    <ThemedView style={styles.container}>
      <ThemedView style={styles.name}>
        <ThemedText type="title2">{name}</ThemedText>
        <View style={styles.button}>
          <Button
            title={isUser ? "Edit" : "DM"}
            // onPress={handleEdit} 
            color="#007BFF" // Customize the button color (Android only)
          />
        </View>
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
        <ThemedText type="title2" style={styles.interestText}>Interests:</ThemedText>
        {interests.map((interest, index) => (
          <TouchableOpacity key={index} style={styles.pill}>
          <Text style={styles.pillText}>{interest}</Text>
          </TouchableOpacity>
        ))}
      </ThemedView>
      <ThemedView style={styles.location}>
        <EventView EventName={eventname} EventDate={eventdate} ProfilePic={profilePic}></EventView>
      </ThemedView>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
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
    backgroundColor: '#007BFF', // Pill background color
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