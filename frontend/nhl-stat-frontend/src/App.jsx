/* App.jsx */

import HomePage from "./pages/Home.jsx";         /* Use for final just testing one at a time */
import PlayerPage from "./pages/PlayerPage.jsx"; <PlayerPage /> 
import { BrowserRouter, Routes, Route } from 'react-router-dom';

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/PlayerPage" element={<PlayerPage />} />
        </Routes>
      </BrowserRouter>
      
    </>
  );
}