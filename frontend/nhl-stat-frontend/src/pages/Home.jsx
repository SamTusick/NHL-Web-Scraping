/* Home Page */
import SelectionButton from '../components/SelectionButton'
import StartButton from '../components/StartButton'
import '../styling/home.css'

export default function HomePage(){
    return (
        <div className="home-container">
            <div className="home-content">
                <h1 className='title'>NHL Stat Web Scraper</h1>
                <div className='selection-button-center'>
                    <div className='selection-button-wrapper'>
                        <SelectionButton label="Get Started" to="/PlayerPage" />
                    </div>  
                </div> 
            </div>
        </div>
    )
}
