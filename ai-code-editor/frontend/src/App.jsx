import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/Login';
import Editor from './pages/Editor';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/editor" element={<Editor />} />
      </Routes>
    </Router>
  );
};

export default App;