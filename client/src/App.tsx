import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import Home from './Home'
import Gallery from './Gallery'
import Navbar from './Navbar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar/>
      <Router>
        <Routes>
          <Route path='/home' element={<Home />} />
          <Route path='/gallery' element={<Gallery />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
