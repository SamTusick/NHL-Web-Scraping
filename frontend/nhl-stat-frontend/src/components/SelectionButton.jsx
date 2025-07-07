/* Selection Buttons Component */

import { Link } from 'react-router-dom'
import '../styling/selectionButton.css'


export default function SelectionButton({label, to}){
    return (
        <Link to={to} >
            <button className="selection-button">
                {label}
            </button>
            </Link>
    )
}