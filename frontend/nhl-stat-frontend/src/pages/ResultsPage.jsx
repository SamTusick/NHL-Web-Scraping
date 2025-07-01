/* Results Page */

import { useLocation } from 'react-router-dom';
import { useEffect, useState } from 'react';
import '../styling/page.css'
import HomeButton from '../components/HomeButton'
import PreviousButton from '../components/PreviousButton'

export default function ResultsPage(){
    const { state } = useLocation();
    const { playerType, statType, count, gameType } = state;

    const [results, setResults] = useState(null);


    useEffect(() => {
        const fetchData = async () => {
            const url = `http://localhost:5000/stats/${playerType}/${statType}?count=${count}&gameType=${encodeURIComponent(gameType)}`;
            try {
                const res = await fetch(url);
                const data = await res.json();
                setResults(data);
            } catch (err) {
                console.error("API error: ", err);
            }
        };

        fetchData();
    }, [playerType, statType, count, gameType]);

    return(
        <>
            <div className="page-content">
                <h1 className='title'>Results</h1>
                <h4 className="sub-title">View Your Results</h4>
            </div>
            <HomeButton />
            <PreviousButton to={`/stats/${playerType}/${statType}`} />

            <div className="results-list">
                {results ? (
                    <>
                        <h3>{results.title}</h3>
                        <ul>
                        {results.leaders.map((player, i) => (
                            <li key={i}>
                            {player.name}: {Object.values(player)[1]}
                            </li>
                        ))}
                        </ul>
                    </>
                ) : (
                    <p>Loading results...</p>
                )}
            </div>            
        </>
    )
}