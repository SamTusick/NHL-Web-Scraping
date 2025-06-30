/* App.jsx */

import AssistStatPage from "./pages/AssistStatPage.jsx";
import GoaliePage from "./pages/GoaliePage.jsx";
import GoalStatPage from "./pages/GoalStatPage.jsx";
import HomePage from "./pages/Home.jsx"
import PlayerPage from "./pages/PlayerPage.jsx"
import PointStatPage from "./pages/PointsStatPage.jsx";
import SkaterPage from "./pages/SkaterPage.jsx"
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import SvStatPage from "./pages/SvStatPage.jsx";

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/PlayerPage" element={<PlayerPage />} />
          <Route path="/skater" element={<SkaterPage />} />
          <Route path="/goalies" element={<GoaliePage />} />

          <Route path="/stats/skater/goals" element={<GoalStatPage />} />
          <Route path="/stats/skater/assists" element={<AssistStatPage />} />
          <Route path="/stats/skater/points" element={<PointStatPage />} />

          <Route path="/stats/goalies/sv" element={<SvStatPage />} />
        </Routes>
      </BrowserRouter>
      
    </>
  );
}