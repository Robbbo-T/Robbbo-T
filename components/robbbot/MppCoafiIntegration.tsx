import React, { useState } from 'react';

const MppCoafiIntegration = () => {
  const [document, setDocument] = useState(null);

  const handleGenerateDocument = async () => {
    try {
      const response = await fetch('http://localhost:8000/generate-document', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: 'Technical Reference Document',
          content: 'This is the content of the technical reference document.',
          metadata: {
            author: 'John Doe',
            date: '2023-01-01',
            version: '1.0',
          },
        }),
      });

      const data = await response.json();
      setDocument(data);
    } catch (error) {
      console.error('Error generating document:', error);
    }
  };

  return (
    <div>
      <h1>MppCoafi Integration</h1>
      <button onClick={handleGenerateDocument}>Generate Document</button>
      {document && (
        <div>
          <h2>Generated Document</h2>
          <pre>{JSON.stringify(document, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default MppCoafiIntegration;
