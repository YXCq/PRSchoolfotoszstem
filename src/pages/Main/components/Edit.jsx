import "../main.css"
import Photo from './Photo.png'
import {Button} from "@chakra-ui/react";

export const Edit = () => {
    return (
        <div className="edit">
            <input type="text" value="Editor of own information" readOnly />
                <div className="editOwnInfo">
                    <form>
                        <img src={Photo} alt=""/>
                        <img src={Photo} alt=""/>
                        <input type="text" value="Full Name:" />
                        <input type="text" value="Phone Number:" />
                        <input type="text" value="E-mail:" />
                        <button type="button" onClick='/'>Save changes</button>
                    </form>
                </div>
        </div>
    )
}