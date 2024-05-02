import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import Home from './Home.jsx'
import Gallery from './Gallery.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
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
