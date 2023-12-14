import Logo from "../../img/dhcompany.png"
import "../main.css"
export const Header = () => {
    return (
        <div className="Header">
            <img src={Logo} alt=""/>
            <h1>Your class is just a click away</h1>
        </div>
    )
}