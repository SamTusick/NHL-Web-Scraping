/* App.jsx */

import HomePage from "./pages/Home.jsx"
import PlayerPage from "./pages/PlayerPage.jsx"
import SkaterPage from "./pages/SkaterPage.jsx"
import { BrowserRouter, Routes, Route } from 'react-router-dom'

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/PlayerPage" element={<PlayerPage />} />
          <Route path="/skaters" element={<SkaterPage />} />
        </Routes>
      </BrowserRouter>
      
    </>
  );
}