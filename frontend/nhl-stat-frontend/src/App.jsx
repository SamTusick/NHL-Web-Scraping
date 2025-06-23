import '../src/styling/App.css'
import StartButton from './components/StartButton';


export default function App() {
  return (
    <>
      <div>
        <h1 className='title'>NHL Stat Web Scraper</h1>
      </div>
      <StartButton></StartButton>
    </>
  );
}