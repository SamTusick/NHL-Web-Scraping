/* Number Input and Slider Component */

import { useState } from "react";
import '../styling/numberSlider.css'

export default function InputAndSlider(){
    const [listNum , setListNum] = useState(10);
    const [seasonType, setSeasonType] = useState("Regular Season");

    return(
        <>
            <div className="control-row">
                <label className="number-input">
                    Number of Skaters: 
                    <input 
                        className="number-content"
                        name="numValue" 
                        type="number" 
                        min={1} 
                        max={100} 
                        value={listNum}
                        onChange={(e) => setListNum(e.target.value)}
                    />
                </label>

                <p className="radio-input">
                    Season Type: 
                    <label className="radio-option">
                        Regular Season
                        <input 
                            name="seasonType"
                            type="radio"
                            value={"Regular Season"}
                            onChange={(e) => setSeasonType(e.target.value)}
                        />
                    </label>
                    <label className="radio-option">
                        Playoffs
                        <input 
                            name="seasonType"
                            type="radio"
                            value={"Playoffs"}
                            onChange={(e) => setSeasonType(e.target.value)}
                        />
                    </label>
                </p>
            </div>
            
            <p className="page-summary">Top {listNum} for The {seasonType} Is Selected</p>
        </>
    )
   
}