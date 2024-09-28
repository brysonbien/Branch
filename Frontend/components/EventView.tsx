import { Image, View, Text, StyleSheet } from 'react-native';
import { useThemeColor } from '@/hooks/useThemeColor';

export type EventViewProp = {
  EventName: string;
  EventDate: string;
  ProfilePic: Array<string>;
  type?: 'default' | 'title' | 'defaultSemiBold' | 'subtitle' | 'link' | 'title2';
};

export default function EventView({
  EventName,
  EventDate,
  ProfilePic
}: EventViewProp) {

  return (
    <View style={styles.container}>
      <View style={styles.roundContainer}>
        <View style={styles.textContainer}>
          <Text style={styles.eventName}>{EventName}</Text>
          <Text style={styles.eventDate}>{EventDate}</Text>
        </View>
        <View style={styles.pictureContainer}>
          {ProfilePic.map((address, index) => (
            <Image
              source={{uri: address}}
              style={styles.picture}
            ></Image>
          ))}
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
    pictureContainer: {
      marginTop: 20,
      alignItems: 'flex-start',
      flexDirection: 'row',
    },
    picture: {
      width: 40,
      height: 40,
      borderRadius: 100,  
    },
    container: {
      flex: 1,
      justifyContent: 'center', // Center the round container
      alignItems: 'center',
    },
    roundContainer: {
      width: 350,               // Set the width of the round container
      height: 150,              // Set the height of the round container
      borderRadius: 25,         // Make it circular
      backgroundColor: '#007BFF', // Background color
      justifyContent: 'flex-start',  // Center text vertically
      elevation: 4,              // Shadow for Android
      shadowColor: '#000',       // Shadow color for iOS
      shadowOffset: { width: 0, height: 2 }, // Shadow offset
      shadowOpacity: 0.2,        // Shadow opacity
      shadowRadius: 4,           // Shadow radius
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
    }
});
