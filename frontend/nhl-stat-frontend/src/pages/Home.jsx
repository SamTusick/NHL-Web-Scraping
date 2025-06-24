/* Home Page */
import StartButton from '../components/StartButton'
import '../styling/home.css'

export default function HomePage(){
    return (
        <div className="home-container">
            <div className="home-content">
                <h1 className='title'>NHL Stat Web Scraper</h1>
                <StartButton />
            </div>
        </div>
    )
}
