/* Goal Stat Page */

import '../styling/page.css'
import InputAndSlider from '../components/NumberSlider'
import HomeButton from '../components/HomeButton'
import PreviousButton from '../components/PreviousButton'

export default function GoalStatPage(){
    return(
        <>
            <div className="page-content">
                <h1 className='title'>Top Skaters - Goals</h1>
                <h4 className='sub-title'>Select The Number of Skaters and Season Type</h4>
            </div>
            <HomeButton />
            <PreviousButton to="/skater" />
            <InputAndSlider />
        </>
    )
}