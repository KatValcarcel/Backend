import React, { useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { getServerInfo } from "./services/user.service";
import { Register } from "./views/Register";
import { Index } from "./views/Index";

function App() {
  useEffect(() => {
    async function miFuncion() {
      const { data } = await getServerInfo()
      console.log(data);
    }
    miFuncion()
  }, [])
  return <Router>
    <Routes>
      <Route path="/" element={<Index />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  </Router>;
}

export default App;
