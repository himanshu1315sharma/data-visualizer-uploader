// NotificationSender.js
import React, { useState } from 'react';
import axios from 'axios';

const NotificationComponent = () => {
  const [message, setMessage] = useState('');

  const sendNotification = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/send_notification', { message });

      if (response.status === 200) {
        // Notification sent successfully
        alert('Notification sent!');
      } else {
        // Handle error response
        alert('Failed to send notification!');
      }
    } catch (error) {
      // Handle network or other errors
      alert('Failed to send notification!');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter notification message"
      />
      <button onClick={sendNotification}>Send Notification</button>
    </div>
  );
};

export default NotificationComponent;

