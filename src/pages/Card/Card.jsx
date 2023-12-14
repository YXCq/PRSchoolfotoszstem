import {Photo} from "./components/Photo";
import "./card.css"
import {CardInfo} from "./components/CardInfo";

export function Card() {
    return (
        <div className="Card">
            <Photo />
            <CardInfo />
        </div>
    )
}