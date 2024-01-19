import {Photo} from "./components/Photo";
import "./card.css"
import {CardInfo} from "./components/CardInfo";

const Card = () => {
    return (
        <div className="Card">
            <Photo />
            <CardInfo />
        </div>
    )
}

export default Card;