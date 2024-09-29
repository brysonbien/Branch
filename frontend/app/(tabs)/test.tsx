import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Chat: React.FC = () => {
    const [messages, setMessages] = useState<any[]>([]);
    const [newMessage, setNewMessage] = useState('');
    const senderId = 1; // Replace with actual sender ID
    const receiverId = 2; // Replace with actual receiver ID

    // Fetch conversation when component mounts
    useEffect(() => {
        fetchConversation();
    }, []);

    // Fetch messages between sender and receiver
    const fetchConversation = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/get_conversation/${senderId}/${receiverId}');
            setMessages(response.data.conversation);
        } catch (error) {
            console.error('Failed to fetch conversation:', error);
        }
    };

    // Send a new message
    const handleSendMessage = async () => {
        try {
            await axios.post('http://127.0.0.1:5000/send_message', {
                sender_id: senderId,
                receiver_id: receiverId,
                message: newMessage
            });
            setNewMessage(''); // Clear input
            fetchConversation(); // Refresh conversation
        } catch (error) {
            console.error('Failed to send message:', error);
        }
    };

    return (
        <div>
            <div>
                {messages.map((msg, index) => (
                    <div key={index}>
                        <strong>{msg.SenderID === senderId ? 'You' : 'Friend'}:</strong> {msg.Message}
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={newMessage}
                onChange={(e) => setNewMessage(e.target.value)}
                placeholder="Type a message..."
            />
            <button onClick={handleSendMessage}>Send</button>
        </div>
    );
};

export default Chat;