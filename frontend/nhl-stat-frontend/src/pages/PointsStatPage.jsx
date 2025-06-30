/* Points Stat Page */

import '../styling/page.css'
import PageInput from '../components/PageInput'
import HomeButton from '../components/HomeButton'
import PreviousButton from '../components/PreviousButton'
import SelectionButton from '../components/SelectionButton'

export default function PointStatPage(){
    return(
        <>
            <div className="page-content">
                <h1 className='title'>Top Skaters - Points</h1>
                <h4 className='sub-title'>Select The Number of Skaters and Season Type</h4>
            </div>
            <HomeButton />
            <PreviousButton to="/skater" />
            <PageInput playerType="Skaters" stat="Points" />
            <div className='selection-button-center'>
                <div className='selection-button-wrapper'>
                    <SelectionButton label="See Results" to="/results" />          
                </div>
            </div>
        </>
    )
}