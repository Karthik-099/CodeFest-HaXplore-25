import React, { useState } from 'react';

const CodeEditor = () => {
  const [code, setCode] = useState('');

  return (
    <textarea
      value={code}
      onChange={(e) => setCode(e.target.value)}
      placeholder="Write your code here..."
    />
  );
};

export default CodeEditor;