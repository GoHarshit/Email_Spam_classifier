import React, { useState } from 'react';
import axios from 'axios';

const EmailClassifier = () => {
  const [emailText, setEmailText] = useState('');
  const [classification, setClassification] = useState('');

  const classifyEmail = async () => {
    try {
      const response = await axios.post('http://localhost:5000/classify', { email: emailText });
      setClassification(response.data.result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <textarea value={emailText} onChange={(e) => setEmailText(e.target.value)} />
      <button onClick={classifyEmail}>Classify</button>
      {classification && <p>{classification}</p>}
    </div>
  );
};

export default EmailClassifier;
