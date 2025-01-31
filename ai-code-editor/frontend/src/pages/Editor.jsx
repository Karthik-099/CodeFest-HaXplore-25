import React from 'react';
import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import CodeEditor from '../components/CodeEditor';

const Editor = () => {
  return (
    <div>
      <Navbar />
      <div className="editor-container">
        <Sidebar />
        <CodeEditor />
      </div>
    </div>
  );
};

export default Editor;