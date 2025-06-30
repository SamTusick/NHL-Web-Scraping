/* Results Page */

import { useParams } from 'react-router-dom';
import '../styling/page.css'
import HomeButton from '../components/HomeButton'
import PreviousButton from '../components/PreviousButton'
import SelectionButton from '../components/SelectionButton'

export default function ResultsPage(){
    const { playerType, statType } = useParams();

    return(
        <>
            <div className="page-content">
                <h1 className='title'>Results</h1>
            </div>
            <HomeButton />
            <PreviousButton to={`/stats/${playerType}/${statType}`} />
        </>
    )
}