# Branch

<img src="images/branch.png" width="500">

##### Bryson Bien - brysonbien@gmail.com - Backend
##### Elliot Willner - elliotwillner@gatech.edu - Database & AI
##### Aditya Singh - adityasht@gmail.com - Backend
##### Feiyang Xie - fxie64@gatech.edu - Frontend

- ### Branch is an interactive application designed to enhance human connections and foster habits that promote positive mental well-being, providing a social tool for helping people branch out.

An app that fosters real-life connections is valuable because it promotes deeper, more meaningful relationships, which are essential for mental and emotional well-being. Unlike digital interactions, face-to-face connections provide trust, empathy, and support, reducing stress and loneliness. Research shows that people with strong in-person networks are happier and healthier. By encouraging these real-life interactions, the app can help build stronger communities, enhance social cohesion, and support overall mental health, making it a powerful tool for positive social change by helping people branch out.

The Harvard Study of Adult Development, one of the longest studies on human happiness, found that close **relationships**, more than money or fame, are what keep people happy throughout their lives. Encouraging people to connect face-to-face can foster a sense of community, reduce social isolation, and promote mental health, making Branch a powerful tool for positive social change.

Branch is a special app that's goal is to get people off the app by enabling users to make plans with real people, in real life, with common interests, therefore fostering these close relationships that will ultimately keep them happy throughout their lives.

## Artificial Intelligence
Branch employs Generative AI to enhance user experience and improve connections by intelligently ranking and suggesting profiles and events based on shared interests using machine learning models to make connections.
- **Better Connections**: By matching users based on shared interests, the platform encourages more meaningful connections.
- **Easily Breanch Out**: Users can find events with a personalized interest-pairing algorithm, fostering stronger communities within the app.
  
## Features
- **Instagram Connection**: Connect your Instagram to for instagrapi to find your mutual following & followers.
- **Event Planning**: Share upcoming events with those around you and branch out. (Also implemented Google Maps API)
- **Who's In Town**: Know which mutuals are in your area, see how long they’ll be around, and arrange meetups.
- **Direct Messaging**: Chat with friends one-on-one or create group chats for planning and catching up.
- **Mental Health and Inclusion**: Promote genuine connections, foster a supportive community, and tackle mental health issues through an inclusive platform.

## How the App Works

Users will sign in with there Instagram account, select their location, interests, and profile photo. Then they ca n start branching out to those around them, with similar interests, and join others or invite people to plans.

### Backend
The backend is built using Python 3, providing a robust and flexible environment for handling all server-side functionalities, such as authentication, messaging, and AI processing.

### Database
The cloud database uses SQL for structured data management and is accessed through AWS, ensuring reliable storage and scalability. It holds data related to users, messages, and any other necessary app entities.

### Login
Login functionality is implemented using Flask to create RESTful client and server applications, with the Instagrapi library used to manage and authenticate user accounts, allowing seamless integration with Instagram services.

### Messaging
Messaging between users is managed through dedicated client-server architecture and handler scripts, enabling real-time communication and interactions within the app.

### Frontend
The frontend is developed using React and TypeScript, providing a dynamic and type-safe environment for building user interfaces and components. This allows for quick iteration and ensures a responsive user experience across all pages and features.

### Generative AI
The Generative AI functionality leverages a Hugging Face large language model (LLM) to match users based on their interests. This AI-powered approach enhances user interactions and social connections allowing users to branch out based on interest-pairing recommendations.

## Technologies
Python, SQL, TypeScript, React Native, AWS, Git, Flask
